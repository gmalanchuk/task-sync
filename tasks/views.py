from rest_framework.viewsets import ModelViewSet

from tasks.models.task_model import Task
from tasks.serializers.task_serializer import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
