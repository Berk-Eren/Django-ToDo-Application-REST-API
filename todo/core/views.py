from django.contrib.auth.decorators import login_required

from rest_framework import authentication, permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="ToDoList API",
        default_version="v1.0.0",
        description="This is the API documentation for ToDo list.",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticated],
    authentication_classes=[authentication.SessionAuthentication],
)


@login_required
def swagger_schema_view(*args, **kwargs):
    return schema_view.with_ui("swagger", cache_timeout=0)(*args, **kwargs)
