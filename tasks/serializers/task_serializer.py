from rest_framework.serializers import ModelSerializer

from tasks.models.task_model import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
