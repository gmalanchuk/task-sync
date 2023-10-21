from django.db import models

from tasks.models.abstract_models import AbsOwnerID, AbsTimeStamp
from tasks.models.board_model import Board


class TaskStatus(AbsTimeStamp, AbsOwnerID):
    title = models.CharField(max_length=16)

    class Meta:
        verbose_name = "TaskStatus"
        verbose_name_plural = "TaskStatus"

    def __str__(self) -> str:
        return f"ID: {self.pk} | Title: {self.title} | Owner: {self.owner_id}"


class Task(AbsTimeStamp, AbsOwnerID):
    board = models.ForeignKey(to=Board, on_delete=models.PROTECT)
    title = models.CharField(max_length=64)
    executor_id = models.IntegerField(null=True, blank=True)
    status = models.ForeignKey(to=TaskStatus, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self) -> str:
        return f"ID: {self.pk} | Title: {self.title}"
