from .models import Task
from .serializers import TaskSerializer
from .filters import IsOwnerOrAssignedPersonFilter
from .permissions import IsOwnerOrAssignedPermission

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated&IsOwnerOrAssignedPermission]
    filter_backends = [IsOwnerOrAssignedPersonFilter]
