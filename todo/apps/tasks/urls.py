from .viewsets import TaskViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', TaskViewSet)
urlpatterns = router.urls
