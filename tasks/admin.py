from django.contrib import admin

from tasks.models.board_model import Board
from tasks.models.column_model import Column
from tasks.models.task_model import Task


admin.site.register(Task)
admin.site.register(Board)
admin.site.register(Column)
