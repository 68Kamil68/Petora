from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

User = get_user_model()


class TestUserView(APITestCase):
    def setUp(self):
        user = User.objects.create_user(
            'testUser', 'test@test.com', 'testpassw12')
        client = APIClient()

    def test_status_create_user(self):
        request = self.client.post(
            '/api/register/', {'username': 'testUser1',
                               'password': 'testpassw12',
                               'email': 'email@email.com'})
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_status_create_user_incorrect_username(self):
        request = self.client.post(
            '/api/register/', {'username': '',
                               'password': 'testpassw12',
                               'email': 'email@email.com'})
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_status_create_user_incorrect_email(self):
        request = self.client.post(
            '/api/register/', {'username': 'testUser23',
                               'password': 'testpassw12',
                               'email': 'emailemail.com'})
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
