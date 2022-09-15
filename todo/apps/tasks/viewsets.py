from .models import Task
from .serializers import TaskSerializer
from .filters import IsOwnerOrAssignedPersonFilter
from .permissions import IsOwnerOrAssignedPermission

from django.conf import settings

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, cache_control
from django.views.decorators.vary import vary_on_headers, vary_on_cookie

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope


@method_decorator(cache_control(private=True), name="dispatch")
@method_decorator(vary_on_cookie, name="dispatch")
@method_decorator(vary_on_headers("Authorization", ), name="dispatch")
@method_decorator(cache_page(settings.CACHE_TTL), name="dispatch")
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated\
                            and IsOwnerOrAssignedPermission]
    filter_backends = [IsOwnerOrAssignedPersonFilter]
