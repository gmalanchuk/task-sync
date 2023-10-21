from django.db import models

from tasks.models.abs_time_stamp import AbsTimeStamp


class Board(AbsTimeStamp):
    title = models.CharField(max_length=32)
    owner_id = models.IntegerField()

    def __str__(self) -> str:
        return f"ID: {self.pk} | Title: {self.title}"
