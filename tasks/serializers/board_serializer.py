from rest_framework.serializers import ModelSerializer

from tasks.models.board_model import Board


class BoardListRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


class BoardPutPatchPostSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
        read_only_fields = ("owner_id",)
