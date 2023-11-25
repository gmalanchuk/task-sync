from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tasks.grpc_services.greeter import check_permission
from tasks.models import Board, Column, Task
from tasks.serializers import BoardSerializer, ColumnSerializer, TaskSerializer


class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("owner_id",)

    def list(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        check_permission()
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
