from rest_framework.serializers import ModelSerializer

from tasks.models.board import Board
from tasks.models.task import Task, TaskStatus


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


class TaskStatusSerializer(ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = "__all__"


class TaskSerializer(ModelSerializer):
    board = BoardSerializer()
    status = TaskStatusSerializer()

    class Meta:
        model = Task
        fields = "__all__"

    def create(self, validated_data: dict) -> Task:
        board_data = validated_data.pop("board")
        status_data = validated_data.pop("status")

        board = Board.objects.create(**board_data)
        status = TaskStatus.objects.create(**status_data)

        task = Task.objects.create(board=board, status=status, **validated_data)

        return task
