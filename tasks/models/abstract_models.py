from django.db import models


class AbsTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbsOwnerIDModel(models.Model):
    owner_id = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True
