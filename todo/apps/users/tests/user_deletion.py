from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

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
        
        self.user = User.objects.get(**response.json())
        token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION="Token %s" % (token))

    def test_user_can_be_deleted(self):
        """
        User can be deleted.
        """
        username = self.user.username
        self.assertEqual(username, "admin")

        delete_url = reverse("user-detail", args=(username, ))

        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, 204)

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username=username)
