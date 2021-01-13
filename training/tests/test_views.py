
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

        )

    def test_practices_view(self):

        response = self.client.get(reverse('pratices'))
        self.assertEqual(response.status_code, 302)

    def test_not_logged_user_cannt_see_page_practices(self):
        response = self.client.get(reverse("pratices"))
        self.assertRedirects(response, "/connecter/?next=/training/practices/")

    def test_logged_user_can_see_page_practices(self):
        user = User.objects.create_user("Juliana," "juliana@dev.io", "some_pass")
        self.client.force_login(user=user)
        response = self.client.get(reverse("pratices"))
        self.assertEqual(response.status_code, 200)

    def test_practice_new_view(self):

        response = self.client.get(reverse('practice-new'))
        self.assertEqual(response.status_code, 302)

    def test_not_logged_user_cannt_see_page_practice_new(self):
        response = self.client.get(reverse("practice-new"))
        self.assertRedirects(response, "/connecter/?next=/training/practices/practice/new/")

    def test_logged_user_can_see_page_practice_new(self):
        user = User.objects.create_user("Juliana," "juliana@dev.io", "some_pass")
        self.client.force_login(user=user)
        response = self.client.get(reverse("practice-new"))
        self.assertEqual(response.status_code, 200)

    def test_practice_detailed_view(self):

        response = self.client.get(self.practice.get_absolute_url())
        self.assertEqual(response.status_code, 302)

    def test_not_logged_user_cannt_see_page_practice_detail(self):
        response = self.client.get(reverse("practice-details", args=[1988]))
        self.assertRedirects(response, "/connecter/?next=/training/practices/practice/1988")
