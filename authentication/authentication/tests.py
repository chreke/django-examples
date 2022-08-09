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
