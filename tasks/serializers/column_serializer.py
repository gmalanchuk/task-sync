from typing import Any

from rest_framework.serializers import ModelSerializer

from tasks.models.column_model import Column


class ColumnListRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Column
        fields = "__all__"


class ColumnPutPatchPostSerializer(ModelSerializer):
    class Meta:
        model = Column
        fields = "__all__"
        read_only_fields = ("owner_id",)

    def create(self, validated_data: dict) -> Any:
        # TODO здесь проставить owner_id
        return super().create(validated_data)
