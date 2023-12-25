from typing import Any

from rest_framework.serializers import ModelSerializer

from tasks.grpc_services.user import get_user_info_by_token
from tasks.models.column_model import Column


class ColumnSerializer(ModelSerializer):
    class Meta:
        model = Column
        fields = "__all__"
        read_only_fields = ("owner_id",)

    def create(self, validated_data: dict) -> Any:
        token = self.context["request"].COOKIES.get("access_token")
        current_user_id = get_user_info_by_token(token)["user_id"]
        validated_data["owner_id"] = current_user_id
        return super().create(validated_data)
