from . import viewsets
from . import views
from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()
router.register("", viewsets.TaskViewSet)
urlpatterns = router.urls
urlpatterns += [path("add/", views.my_view)]
