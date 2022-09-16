from .models import Task
from todo.apps.comments.models import Comment

from django.contrib import admin


class CommentInline(admin.TabularInline):
    model = Comment


class TaskAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    empty_value_display = "unknown"
    list_display = (
        "name",
        "state",
        "task_id",
        "task_creator",
        "task_assigned_to",
    )
    fields = (
        "name",
        "state",
        (
            "created_by",
            "assigned_to",
        ),
    )

    @admin.display(description="Task's Id")
    def task_id(self, obj):
        return obj.id


admin.site.register(Task, TaskAdmin)
