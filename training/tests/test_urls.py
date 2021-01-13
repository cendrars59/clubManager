from django.test import SimpleTestCase
from django.urls import resolve, reverse

from training.urls import *
from training.views import *


class TestTraingPracticeUrls(SimpleTestCase):

    # Checking home practices is resolved
    def test_practices_url_is_resolved(self):
        resolver = resolve('/training/practices/')
        self.assertEqual(resolver.view_name, 'pratices')
        url = reverse('pratices')
        self.assertEqual(url, '/training/practices/')

    # Checking new practice url is resolved

    def test_new_url_is_resolved(self):
        resolver = resolve('/training/practices/practice/new/')
        self.assertEqual(resolver.view_name, 'practice-new')
        url = reverse('practice-new')
        self.assertEqual(url, '/training/practices/practice/new/')

    # Checking URL edit is resolved
    def test_edit_url_is_resolved(self):
        url = reverse('practice-update', args=[1988])
        self.assertEqual(url, '/training/practices/practice/edit/1988')

    # Checking URL detail is resolved

    def test_detail_url_is_resolved(self):
        url = reverse('practice-details', args=[1988])
        self.assertEqual(url, '/training/practices/practice/1988')
