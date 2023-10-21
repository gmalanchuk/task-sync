from rest_framework.serializers import ModelSerializer

from tasks.models.board_model import Board


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
