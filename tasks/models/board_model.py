from django.db import models

from tasks.models.abstract_models import AbsOwnerIDModel, AbsTimeStampModel


class Board(AbsTimeStampModel, AbsOwnerIDModel):
    title = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    def __str__(self) -> str:
        return f"ID: {self.pk} | Title: {self.title}"
