from rest_framework import filters


class IsOwnerOrSuperuserFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset if request.user.is_superuser\
                            else queryset.filter(id=request.user.id)
