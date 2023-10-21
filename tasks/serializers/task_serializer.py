from rest_framework.serializers import ModelSerializer

from tasks.models.board_model import Board
from tasks.models.task_model import Task
from tasks.serializers.board_serializer import BoardSerializer


class TaskSerializer(ModelSerializer):
    board = BoardSerializer()

    class Meta:
        model = Task
        fields = "__all__"

    def create(self, validated_data: dict) -> Task:
        board_data = validated_data.pop("board")

        board = Board.objects.create(**board_data)

        task = Task.objects.create(board=board, **validated_data)

        return task
