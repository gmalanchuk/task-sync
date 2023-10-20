from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"ID: {self.pk} | Title: {self.title}"


# class TaskStatus(models.Model):
#     status = models.CharField(max_length=16)
