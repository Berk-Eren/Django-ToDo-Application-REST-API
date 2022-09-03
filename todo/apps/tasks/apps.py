from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    label = 'tasks'
    name = 'todo.apps.tasks'
