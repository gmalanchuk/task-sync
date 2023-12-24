from datetime import datetime, timedelta

from rest_framework import serializers

from tasks.celery_tasks import celery_calendar_notification
from tasks.grpc_services.user import get_user_info
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
        task = Task.objects.create(**validated_data)

        token = self.context["request"].COOKIES.get("access_token")
        task.owner_id = get_user_info(token)["user_id"]

        for tag in self.tags:
            tag_obj, _ = Tag.objects.get_or_create(title=tag)
            task.tags.add(tag_obj)

        task.save()
        if task.deadline:
            eta_time = datetime.utcnow() + timedelta(seconds=15)
            celery_calendar_notification.apply_async(args=(task.deadline,), eta=eta_time)

        return task
