from django.contrib import admin

from tasks.models.board_model import Board
from tasks.models.task_model import Task, TaskStatus


admin.site.register(Task)
admin.site.register(TaskStatus)
admin.site.register(Board)
