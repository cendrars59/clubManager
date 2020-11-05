from django.test import SimpleTestCase
from django.urls import resolve, reverse

from pages.views import home, mentions


class TestUrls(SimpleTestCase):

    # Checking URL homepage is resolved
    def test_homepage_url_is_resolved(self):
        url = reverse('pages:home')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)


    def test_home_url_is_found(self):
        # Issue a GET request.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    # Checking URL mentions is resolved
    def test_mentions_url_is_resolved(self):
        url = reverse('pages:mentions')
        print(resolve(url))
        self.assertEqual(resolve(url).func, mentions)

    def test_mentions_url_is_found(self):
        # Issue a GET request.
        response = self.client.get('/mentions')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
  