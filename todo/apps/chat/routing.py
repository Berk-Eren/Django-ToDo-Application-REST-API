from django.urls import re_path

from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/chat/user/(?P<single_name>\w+)', consumers.UserConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>\w+)', consumers.ChatConsumer.as_asgi()),
]