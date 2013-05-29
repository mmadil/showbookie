from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from .models import UserProfile


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = UserProfile

