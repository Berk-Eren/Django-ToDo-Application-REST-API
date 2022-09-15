"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from todo.apps.tasks.views import my_view
from todo.core.views import swagger_schema_view

from two_factor.urls import urlpatterns as tf_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include("todo.apps.tasks.urls")),
    path('users/', include("todo.apps.users.urls")),
    path('swagger/', swagger_schema_view,#schema_view.with_ui('swagger', cache_timeout=0),
                        name='schema-swagger-ui'),
    path('oauth/', include('oauth2_provider.urls',
                                namespace="oauth-provider")),
    path('__debug__/', include('debug_toolbar.urls')),
    path("add/", my_view),
    path('', include(tf_urls))
]
