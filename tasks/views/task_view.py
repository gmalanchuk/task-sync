from typing import Any

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from tasks.permissions import is_admin_or_owner_user, is_authenticated_user
from tasks.serializers import TaskListRetrieveSerializer, TaskPutPatchPostSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all().prefetch_related("tags")
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("column",)

    def get_serializer_class(self) -> type[TaskPutPatchPostSerializer] | type[TaskListRetrieveSerializer]:
        if self.request.method in ("PUT", "PATCH", "POST"):
            return TaskPutPatchPostSerializer
        else:
            return TaskListRetrieveSerializer

    @is_authenticated_user
    def create(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        return super().create(request, *args, **kwargs)

    @is_admin_or_owner_user(queryset)
    def update(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        return super().update(request, *args, **kwargs)

    @is_admin_or_owner_user(queryset)
    def partial_update(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        return super().partial_update(request, *args, **kwargs)

    @is_admin_or_owner_user(queryset)
    def destroy(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        return super().destroy(request, *args, **kwargs)
