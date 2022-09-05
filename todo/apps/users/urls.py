from .viewsets import UserViewSet

from rest_framework import routers


router = routers.SimpleRouter()
router.register('', UserViewSet)
urlpatterns = router.urls
