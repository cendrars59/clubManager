from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import resolve, reverse

from users.views import register


class TestUsersViews(TestCase):

    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

    # Checking register is found
    def test_register_view_is_found(self):
        # Issue a GET request.
        client = Client()
        response = client.get(reverse('register'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    # Checking login is found
    def test_login_view_is_found(self):
        client = Client()
        response = client.get(reverse('login'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    # Checking login data handling

    # Checking logout is found

    def test_logout_view_is_found(self):
        client = Client()
        response = client.get(reverse('logout'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/logout.html')

    # Checking redirect if attempt to access to profile without being logged in
    def test_redirect_if_not_logged_to_access_to_profile(self):
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, '/connecter/?next=/profile/')

    def test_correctly_logged_in(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('home'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
