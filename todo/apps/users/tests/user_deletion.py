from django.urls import reverse

from rest_framework.test import APITestCase

from todo.apps.users.models import User


class UserDeletion(APITestCase):
    def setUp(self):
        self.url = reverse("user-list")

        user_info = {
            "username": "admin",
            "password": "admin",
            "password2": "admin"
        }
        
        response = self.client.post(self.url, user_info)
        self.user = User.objects.get(**response)
