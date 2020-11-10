from django.test import SimpleTestCase
from django.urls import resolve, reverse

from pages.views import home, mentions


class TestPagesUrls(SimpleTestCase):

    # Checking home is resolved
    def test_home_url_is_resolved(self):
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'home')

    # Checking URL mentions is resolved

    def test_mentions_url_is_resolved(self):
        resolver = resolve('/mentions')
        self.assertEqual(resolver.view_name, 'mentions')
