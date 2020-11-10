from django.test import Client, TestCase
from django.urls import resolve, reverse

from pages.views import home, mentions


class TestPagesViews(TestCase):

    # Checking home is found
    def test_home_views(self):
        # Issue a GET request.
        client = Client()
        response = client.get(reverse('home'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')

    # Checking mentions is found

    def test_mentions_views(self):
        client = Client()
        response = client.get(reverse('mentions'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/mentions.html')
