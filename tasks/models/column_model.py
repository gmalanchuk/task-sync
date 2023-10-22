from django.db import models

from tasks.models.abstract_models import AbsOwnerIDModel, AbsTimeStampModel
from tasks.models.board_model import Board


class Column(AbsTimeStampModel, AbsOwnerIDModel):
    title = models.CharField(max_length=32)
    board = models.ForeignKey(to=Board, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Column"
        verbose_name_plural = "Columns"

    def __str__(self) -> str:
        return f"ID: {self.pk} | Title: {self.title}"
