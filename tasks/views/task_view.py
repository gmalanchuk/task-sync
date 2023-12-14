from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all().prefetch_related("tags")
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("column",)
