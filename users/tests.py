from django.test import TestCase
from django.urls import reverse
from .models import Users


class UserModelTest(TestCase):
    def test_user_creation(self):
        user = Users.objects.create(name="John Doe", email="john@example.com")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john@example.com")


class UserViewsTest(TestCase):
    def setUp(self):
        self.user = Users.objects.create(name="Jane Smith", email="jane@example.com")

    def test_user_list_view(self):
        response = self.client.get(reverse("user-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.name)

    def test_user_create_view_get(self):
        response = self.client.get(reverse("user-create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create")  # check for a word in your form

    def test_user_create_view_post(self):
        data = {"name": "Alice", "email": "alice@example.com"}
        response = self.client.post(reverse("user-create"), data)
        self.assertEqual(response.status_code, 302)  # redirect after success
        self.assertTrue(Users.objects.filter(email="alice@example.com").exists())
