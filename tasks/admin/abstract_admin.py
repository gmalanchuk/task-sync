from django.contrib import admin


class AbsTimeStampAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
