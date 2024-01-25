from typing import Any

from rest_framework.serializers import ModelSerializer

from tasks.grpc_services import get_user_info_by_token
from tasks.models.board_model import Board


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
        read_only_fields = ("owner_id",)

    def create(self, validated_data: dict) -> Any:
        current_user_id = get_user_info_by_token(self.context["request"])["user_id"]
        validated_data["owner_id"] = current_user_id
        return super().create(validated_data)
