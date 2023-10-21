from rest_framework.viewsets import ModelViewSet

from tasks.models.task import Task
from tasks.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
