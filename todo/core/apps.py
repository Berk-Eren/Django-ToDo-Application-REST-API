from django.apps import AppConfig


class UsersConfig(AppConfig):
    default = True
    default_auto_field = "django.db.models.BigAutoField"
    label = "core"
    name = "todo.apps.core"
