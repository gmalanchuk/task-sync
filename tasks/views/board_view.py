from typing import Any

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from config.celery import test1, test2
from tasks.models import Board
from tasks.permissions import is_admin_or_owner_user, is_authenticated_user
from tasks.rabbitmq.notifications import event_notification
from tasks.serializers import BoardSerializer


class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("owner_id",)

    def list(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        test1.delay()
        test2.delay()
        return super().list(request, *args, **kwargs)

    @event_notification(queryset=queryset)
    @is_authenticated_user
    def create(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        return super().create(request, *args, **kwargs)

    @event_notification(queryset=queryset)
    @is_admin_or_owner_user(queryset=queryset)
    def update(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        return super().update(request, *args, **kwargs)

    @event_notification(queryset=queryset)
    @is_admin_or_owner_user(queryset=queryset)
    def partial_update(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        return super().partial_update(request, *args, **kwargs)

    @event_notification(queryset=queryset)
    @is_admin_or_owner_user(queryset=queryset)
    def destroy(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        return super().destroy(request, *args, **kwargs)
