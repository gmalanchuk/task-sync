from django.contrib import admin

from tasks.admin.abstract_admin import AbsTimeStampAdmin
from tasks.models import Board


@admin.register(Board)
class BoardAdmin(AbsTimeStampAdmin):
    pass
