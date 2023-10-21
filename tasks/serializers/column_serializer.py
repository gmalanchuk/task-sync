from rest_framework.serializers import ModelSerializer

from tasks.models.column_model import Column


class ColumnSerializer(ModelSerializer):
    class Meta:
        model = Column
        fields = "__all__"
