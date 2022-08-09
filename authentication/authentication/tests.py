from django.contrib.auth.models import User
from rest_framework.test import APITestCase

class CreateAccountTest(APITestCase):

    def test_create_account(self):
        response = self.client.post(
            "/accounts/",
            {
                "username": "foobar",
                "password": "Supersecret!@#$",
            }
        )
        self.assertEqual(response.status_code, 201)


class LoginTest(APITestCase):

    def setUp(self):
        self.username = "foobar"
        self.password = "Supersecret!@#$"
        User.objects.create_user(
            username=self.username,
            password=self.password,
        )

    def test_login(self):
        response = self.client.post(
            "/sessions/",
            {
                "username": self.username,
                "password": self.password,
            }
        )
        token = response.json().get("token")
        self.assertIsNotNone(token)
