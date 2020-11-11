from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegisterUserForm(UserCreationForm):

    # Need to be declared because not part of the standard form
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):

    # Need to be declared because not part of the standard form
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'mobile_phone']
