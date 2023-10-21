from django.contrib import admin

from tasks.models.board import Board
from tasks.models.task import Task, TaskStatus


admin.site.register(Task)
admin.site.register(TaskStatus)
admin.site.register(Board)
