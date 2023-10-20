from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=64)


# class TaskStatus(models.Model):
#     status = models.CharField(max_length=16)
