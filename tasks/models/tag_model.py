from django.db import models

from tasks.models.abstract_models import AbsOwnerIDModel, AbsTimeStampModel


class Tag(AbsTimeStampModel, AbsOwnerIDModel):
    title = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self) -> str:
        return f"ID: {self.pk} | Title: {self.title}"
