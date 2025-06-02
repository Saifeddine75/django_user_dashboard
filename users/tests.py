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


    def test_user_update_view(self):
        url = reverse("user-update", args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.name)

        updated_data = {
            "name": "Jane Updated",
            "email": self.user.email,
        }
        response = self.client.post(url, updated_data)
        self.assertEqual(response.status_code, 302)

        self.user.refresh_from_db()
        self.assertEqual(self.user.name, "Jane Updated")

    def test_user_delete_view(self):
        url = reverse("user-delete", args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "delete")

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Users.objects.filter(pk=self.user.pk).exists())