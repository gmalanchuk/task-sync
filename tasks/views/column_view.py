from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from tasks.models import Column
from tasks.serializers import ColumnSerializer


class ColumnViewSet(ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("board",)
