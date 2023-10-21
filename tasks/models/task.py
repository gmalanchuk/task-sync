from django.db import models

from tasks.models.abs_time_stamp import AbsTimeStamp
from tasks.models.board import Board


class TaskStatus(AbsTimeStamp):
    title = models.CharField(max_length=16)
    owner_id = models.IntegerField()

    class Meta:
        verbose_name = "TaskStatus"
        verbose_name_plural = "TaskStatus"

    def __str__(self) -> str:
        return f"ID: {self.pk} | Title: {self.title} | Owner: {self.owner_id}"


class Task(AbsTimeStamp):
    board = models.ForeignKey(to=Board, on_delete=models.PROTECT)
    title = models.CharField(max_length=64)
    owner_id = models.IntegerField()
    executor_id = models.IntegerField(null=True, blank=True)
    status = models.ForeignKey(to=TaskStatus, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"ID: {self.pk} | Title: {self.title}"
