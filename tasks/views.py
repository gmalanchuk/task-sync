from typing import Any

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from tasks.models import Board, Column, Task
from tasks.permissions.is_authenticated import is_authenticated_user
from tasks.serializers import BoardSerializer, ColumnSerializer, TaskSerializer


class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("owner_id",)

    @is_authenticated_user
    def list(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        return super().list(request, *args, **kwargs)


class ColumnViewSet(ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("board",)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all().prefetch_related("tags")
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("column",)
