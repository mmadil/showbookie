from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from .models import UserProfile


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class UserProfileUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture','birth_date','facebook','twitter','bio')
