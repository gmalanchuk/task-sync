from django.contrib import admin

from tasks.admin.abstract_admin import AbsTimeStampAdmin
from tasks.models.tag_model import Tag


@admin.register(Tag)
class TagAdmin(AbsTimeStampAdmin):
    pass
