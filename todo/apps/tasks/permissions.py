from django.db.models import Q
from rest_framework import permissions


class IsOwnerOrAssignedPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS)\
                or request.user.is_superuser:
            return True
        return obj.assigned_to == request.user\
                or obj.created_by == request.user
