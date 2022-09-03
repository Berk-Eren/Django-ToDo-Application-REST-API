from django.db import models
from django.conf import settings

from todo.apps.tasks.models import Task


class Comment(models.Model):
    comment_of = models.ForeignKey("self", related_name="subcomments", 
                                        blank=True, null=True, 
                                            on_delete=models.SET_NULL)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        related_name="comments",
                                            blank=True, null=True,
                                            on_delete=models.SET_NULL)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
