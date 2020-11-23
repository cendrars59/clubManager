from django.contrib.auth.models import User
from django.db import models
from django.test import TestCase
from django.utils import timezone

from training.models import Practice


class PracticeModelTests(TestCase):

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

    def test_practice_listing(self):

        self.assertEqual(f'{self.practice.title}', 'Test Model Title')
        self.assertEqual(f'{self.practice.author}', 'elvis')
        self.assertEqual(f'{self.practice.description}', 'description model')
        self.assertEqual(f'{self.practice.material}', 'material required for practice')
        self.assertEqual(f'{self.practice.photo1}', 'default_practice.png')
        self.assertEqual(f'{self.practice.photo2}', 'default_practice.png')
        self.assertEqual(f'{self.practice.photo3}', 'default_practice.png')
