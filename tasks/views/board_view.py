from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tasks.grpc_services import get_user_info_by_token
from tasks.models import Board
from tasks.permissions import is_admin_or_owner_user, is_admin_user, is_authenticated_user
from tasks.rabbitmq.notifications import event_notification
from tasks.serializers import BoardSerializer


class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    @action(detail=False, methods=["get"], description="Get all boards where the user is owner")
    def owner_boards(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        user_id = get_user_info_by_token(request)["user_id"]
        queryset = self.get_queryset().filter(owner_id=user_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], description="Get all tables where the user is whitelisted")
    def whitelist_boards(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        user_id = get_user_info_by_token(request)["user_id"]
        queryset = self.get_queryset().filter(whitelist__contains=[user_id])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @is_admin_user
    def list(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().list(request, *args, **kwargs)

    @event_notification(queryset=queryset)
    @is_authenticated_user
    def create(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().create(request, *args, **kwargs)

    @event_notification(queryset=queryset)
    @is_admin_or_owner_user(queryset=queryset)
    def update(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().update(request, *args, **kwargs)

    @event_notification(queryset=queryset)
    @is_admin_or_owner_user(queryset=queryset)
    def partial_update(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().partial_update(request, *args, **kwargs)

    @event_notification(queryset=queryset)
    @is_admin_or_owner_user(queryset=queryset)
    def destroy(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().destroy(request, *args, **kwargs)
