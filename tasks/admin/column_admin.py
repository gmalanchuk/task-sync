from django.contrib import admin

from tasks.admin.abstract_admin import AbsTimeStampAdmin
from tasks.models import Column


@admin.register(Column)
class ColumnAdmin(AbsTimeStampAdmin):
    pass
