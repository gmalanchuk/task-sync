from typing import Any

from rest_framework.serializers import ModelSerializer

from tasks.models.board_model import Board


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
        read_only_fields = ("owner_id",)

    def create(self, validated_data: dict) -> Any:
        # TODO здесь проставить owner_id
        return super().create(validated_data)
