from .models import User
from .validators import checkPasswordsAreAEqualIfExist, checkPasswordsAreIncludedAndEqual

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
                    write_only=True, 
                    required=False, 
                    style={"input_type": "password"}
                )

    class Meta:
        model = User
        exclude = (
            "id",
            "groups",
            "user_permissions",
        )
        read_only_fields = (
            "date_joined",
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
        )
        extra_kwargs = {"password": {"write_only": True, "required": False}}

    def create(self, validated_data):
        checkPasswordsAreIncludedAndEqual(validated_data)
        validated_data.pop("password2")

        return super().create(validated_data)

    def update(self, instance, validated_data):
        checkPasswordsAreAEqualIfExist(validated_data)
        validated_data.pop("password2", None)

        return super().update(instance, validated_data)
