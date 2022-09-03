from django.db import models
from django.conf import settings
from django.contrib import admin
from django.db.models.functions import Concat


class TaskStatuses(models.TextChoices):
        TO_DO = 'TD', 'To Do'
        IN_PROGRESS = 'IP', 'In Progress'
        DONE = 'D', 'Done'


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=False)
    state = models.CharField(max_length=5,
                                choices=TaskStatuses.choices,
                                    default=TaskStatuses.TO_DO)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        related_name="has_created_tasks",
                                            blank=True, null=True,
                                                on_delete=models.SET_NULL)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        related_name="assigned_tasks",
                                            blank=True, null=True,
                                                on_delete=models.SET_NULL)

    @admin.display(ordering="name")
    def task_name(self):
        return self.name + "hre"
