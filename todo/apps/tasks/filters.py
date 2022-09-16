from django.db.models import Q
from rest_framework import filters


class IsOwnerOrAssignedPersonFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_superuser:
            return queryset
        return queryset.filter(Q(created_by=request.user) | Q(assigned_to=request.user))
