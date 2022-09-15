from .models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={
                    "input_type": "password"
                })

    class Meta:
        model = User
        exclude = ('id', 'groups', 'user_permissions', )
        read_only_fields = ('date_joined', 'is_staff', 'is_active', 
                                'is_superuser', 'last_login', )
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate(self, data):
        password2 = data.pop("password2")

        if data["password"] != password2:
            raise serializers.ValidationError(
                "'password' and 'password2' should be equal to each other."
            )
        
        return super().validate(data)

    #def save(self, ):