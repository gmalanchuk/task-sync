from django.db import models


class AbsTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbsOwnerID(models.Model):
    owner_id = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True
