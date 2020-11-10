from django.test import SimpleTestCase
from django.urls import resolve, reverse

from users.views import register


class TestUsersUrls(SimpleTestCase):

    # Checking home is resolved
    def test_register_url_is_resolved(self):
        resolver = resolve('/enregistrer/')
        self.assertEqual(resolver.view_name, 'register')

    # Checking URL mentions is resolved
    def test_login_url_is_resolved(self):
        resolver = resolve('/connecter/')
        self.assertEqual(resolver.view_name, 'login')

    # Checking URL mentions is resolved
    def test_logout_url_is_resolved(self):
        resolver = resolve('/quitter/')
        self.assertEqual(resolver.view_name, 'logout')
