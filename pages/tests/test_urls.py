from django.test import SimpleTestCase
from django.urls import resolve, reverse

#from pages.views import home, mentions

from django.test import Client


class TestUrls(SimpleTestCase):

    # Checking URL homepage is resolved
    #def test_homepage_url_is_resolved(self):
    #    url = reverse('home')
    #    self.assertEqual(resolve(url).func, home)

    # Checking URL mentions is resolved
    #def test_mentions_url_is_resolved(self):
    #    url = reverse('mentions')
    #    self.assertEqual(resolve(url).func, mentions)
    # Checking URL homepage is resolved

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)