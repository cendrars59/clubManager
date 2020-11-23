
from django.contrib.auth.models import User
from django.db import models
from django.test import Client, TestCase
from django.urls import reverse

from training.models import Practice
from training.urls import *
from training.views import *


class PracticeViewTests(TestCase):

    def setUp(self):

        self.user = User.objects.create(
            username='elvis',
            email='elvis@isnotdead.com'
        )

        self.practice = Practice.objects.create(
            title='Test Model Title',
            author=self.user,
            description='description model',
            material='material required for practice'

        )

    def test_practices_view(self):

        response = self.client.get(reverse('pratices'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'training/practice_list.html')

    def test_practice_new_view(self):

        response = self.client.get(reverse('practice-new'))
        self.assertEqual(response.status_code, 302)

    def test_practice_detailed_view(self):

        response = self.client.get(self.practice.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'training/practice_detail.html')
