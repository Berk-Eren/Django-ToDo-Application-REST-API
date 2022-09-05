from .models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id', 'groups', 'user_permissions',)
        read_only_fields = ('date_joined', 'is_staff', 'is_active', 
                                'is_superuser', 'last_login', )
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }