from django.contrib.auth.models import User
from django.db import models
from django.test import TestCase
from django.utils import timezone

from training.models import Category, Practice


class PracticeModelTests(TestCase):

    def setUp(self):

        self.user = User.objects.create(
            username='elvis',
            email='elvis@isnotdead.com'
        )

        self.practice = Practice.objects.create(
            title='Test Model Title',
            author=self.user,
            description='description model'

        )

    def test_practice_listing(self):

        self.assertEqual(f'{self.practice.title}', 'Test Model Title')
        self.assertEqual(f'{self.practice.author}', 'elvis')
        self.assertEqual(f'{self.practice.description}', 'description model')


class CategoryModelTests(TestCase):

    def setUp(self):

        self.user = User.objects.create(
            username='elvis',
            email='elvis@isnotdead.com'
        )

        self.category = Category.objects.create(
            title='Test Model Category Title',
            author=self.user,
            description='description category model'

        )

    def test_category_listing(self):

        self.assertEqual(f'{self.category.title}', 'Test Model Category Title')
        self.assertEqual(f'{self.category.author}', 'elvis')
        self.assertEqual(f'{self.category.description}', 'description category model')
