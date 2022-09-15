from .models import User
from .serializers import UserSerializer
from .filters import IsOwnerOrSuperuserFilter

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [IsOwnerOrSuperuserFilter]
