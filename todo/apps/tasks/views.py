from rest_framework.decorators import api_view
from rest_framework.response import Response

# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import AllowAny

from .tasks import add

# @permission_classes([AllowAny])
@api_view(
    [
        "GET",
    ]
)
def my_view(request, format=None):
    add.delay(2, 3)
    return Response({"hello": 12})
