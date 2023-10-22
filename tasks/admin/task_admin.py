from django.contrib import admin

from tasks.admin.abstract_admin import AbsTimeStampAdmin
from tasks.models import Task


@admin.register(Task)
class TaskAdmin(AbsTimeStampAdmin):
    pass
