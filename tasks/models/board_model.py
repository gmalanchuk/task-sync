from django.contrib.postgres.fields import ArrayField
from django.db import models

from tasks.models.abstract_models import AbsOwnerIDModel, AbsTimeStampModel


class Board(AbsTimeStampModel, AbsOwnerIDModel):
    title = models.CharField(max_length=32)
    whitelist = ArrayField(
        models.IntegerField(), blank=True, null=True
    )  # Identifiers of users who have access to the board

    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    def __str__(self) -> str:
        return f"ID: {self.pk} | Title: {self.title}"
