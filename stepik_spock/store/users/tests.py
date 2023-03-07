from http import HTTPStatus
from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.forms import UserRegisterForm
from users.models import User, EmailVerification


class UserRegisterViewTestCase(TestCase):
    def setUp(self):
        self.path = reverse('users:register')
        self.data = {
            'first_name': 'Narek', 'last_name': 'Testov',
            'username': 'testuser', 'email': 'testemail@meliksetyan.ru',
            'password1': '12345678pP', 'password2': '12345678pP',
        }
    
    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_post_success(self):
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, data=self.data)

        # Check creating of a new user
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        # Check creating of email verification object
        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date()
        )

    def test_user_registration_post_fail(self):
        username = self.data['username']
        User.objects.create(username=username)

        response = self.client.post(self.path, data=self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)