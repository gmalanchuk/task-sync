from django.db import models

from tasks.models.abstract_models import AbsOwnerIDModel, AbsTimeStampModel
from tasks.models.column_model import Column


class Task(AbsTimeStampModel, AbsOwnerIDModel):
    title = models.CharField(max_length=64)
    executor_id = models.IntegerField(null=True, blank=True)
    column = models.ForeignKey(to=Column, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self) -> str:
        return f"ID: {self.pk} | Title: {self.title}"
