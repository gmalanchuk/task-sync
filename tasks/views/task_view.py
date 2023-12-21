from typing import Any

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from tasks.permissions import is_admin_or_owner_user, is_authenticated_user
from tasks.rabbitmq.notifications import event_notification
from tasks.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all().prefetch_related("tags")
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("column",)

    @event_notification(queryset=queryset)
    @is_authenticated_user
    def create(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        return super().create(request, *args, **kwargs)

    @event_notification(queryset=queryset)
    @is_admin_or_owner_user(queryset)
    def update(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        return super().update(request, *args, **kwargs)

    @event_notification(queryset=queryset)
    @is_admin_or_owner_user(queryset)
    def partial_update(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        return super().partial_update(request, *args, **kwargs)

    @event_notification(queryset=queryset)
    @is_admin_or_owner_user(queryset)
    def destroy(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        return super().destroy(request, *args, **kwargs)
