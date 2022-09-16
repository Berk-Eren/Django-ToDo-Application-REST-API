import imp
from re import I
from .models import Task
from rest_framework import serializers


class AssignedToRelation(serializers.RelatedField):
    queryset = Task.objects.all()

    def to_representation(self, value):
        return value.username if value.username else "unknown"

    def to_internal_value(self, data):
        return super().to_internal_value(data)
