from .models import Task
from .relations import AssignedToRelation

from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    #created_by = serializers.HyperlinkedRelatedField(read_only=True, 
    #                                                    view_name="user-detail")
    #assigned_to = AssignedToRelation()
    #assigned_to = serializers.HyperlinkedRelatedField(read_only=True, 
    #                                                    view_name="user-detail")

    class Meta:
        model = Task
        #exclude = ("id", )
        fields = ('url', 'name', 'assigned_to', 'created_by', )

    def save(self, *args, **kwargs):
        request = self.context["request"]
        self.initial_data["created_by"] = request.user.id
        super().save(*args, **kwargs)

    def validate_name(self, data):
        return data
