from datetime import datetime, timedelta, timezone

from rest_framework import serializers

from tasks.celery_tasks import celery_calendar_notification
from tasks.grpc_services.user import get_user_info_by_id, get_user_info_by_token
from tasks.models.tag_model import Tag
from tasks.models.task_model import Task


class TaskSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, slug_field="title", required=False, queryset=Tag.objects.all())

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ("owner_id",)

    def is_valid(self, *, raise_exception: bool = False) -> bool:
        self.tags = self.initial_data.pop("tags", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data: dict) -> Task:
        if validated_data.get("deadline"):
            if validated_data["deadline"] < (datetime.utcnow() + timedelta(hours=1)).replace(tzinfo=timezone.utc):
                raise serializers.ValidationError(
                    {"deadline": ["The deadline must be no earlier than one hour after the task is created"]}
                )

        task = Task.objects.create(**validated_data)

        token = self.context["request"].COOKIES.get("access_token")
        user_info = get_user_info_by_token(token)
        task.owner_id = user_info["user_id"]

        for tag in self.tags:
            tag_obj, _ = Tag.objects.get_or_create(title=tag)
            task.tags.add(tag_obj)

        if task.deadline:
            eta_time = datetime.utcnow()  # todo task.deadline - datetime.utcnow(hours=1)
            recipient_email = get_user_info_by_id(user_id=task.executor_id)["email"]
            celery_calendar_notification.apply_async(
                args=(task.id, user_info["username"], recipient_email, Task.__name__), eta=eta_time
            )

        task.save()
        return task
