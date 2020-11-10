from django.test import TestCase

from users.forms import RegisterUserForm


class TestRegisterUserForm(TestCase):

    def test_user_form_is_valid(self):

        form = RegisterUserForm(
            data={
                'username': 'elvis',
                'email': 'elvis@isnotdead.com',
                'password1': 't0t0ll@1',
                'password2': 't0t0ll@1'
            }
        )
        self.assertTrue(form.is_valid())

    def test_user_form_is_empty(self):

        form = RegisterUserForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_user_form_user_name_is_empty(self):

        form = RegisterUserForm(
            data={
                'username': '',
                'email': 'elvis@isnotdead.com',
                'password1': 't0t0ll@1',
                'password2': 't0t0ll@1'
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_user_form_email_is_empty(self):

        form = RegisterUserForm(
            data={
                'username': 'elvis',
                'email': '',
                'password1': 't0t0ll@1',
                'password2': 't0t0ll@1'
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_user_form_email_is_not_valid(self):

        form = RegisterUserForm(
            data={
                'username': 'elvis',
                'email': 'elvis.com',
                'password1': 't0t0ll@1',
                'password2': 't0t0ll@1'
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_user_form_pwd1_is_empty(self):

        form = RegisterUserForm(
            data={
                'username': 'elvis',
                'email': 'elvis@isnotdead.com',
                'password1': '',
                'password2': 't0t0ll@1'
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_user_form_pwd2_is_empty(self):

        form = RegisterUserForm(
            data={
                'username': 'elvis',
                'email': 'elvis@isnotdead.com',
                'password1': 't0t0ll@1',
                'password2': ''
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
