from rest_framework import serializers

from tasks.models.tag_model import Tag
from tasks.models.task_model import Task


class TaskSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, slug_field="title", required=False, queryset=Tag.objects.all())

    class Meta:
        model = Task
        fields = "__all__"

    def is_valid(self, *, raise_exception: bool = False) -> bool:
        self.tags = self.initial_data.pop("tags", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data: dict) -> Task:
        task = Task.objects.create(**validated_data)

        for tag in self.tags:
            tag_obj, _ = Tag.objects.get_or_create(title=tag)
            task.tags.add(tag_obj)

        task.save()
        return task
