from .models import UserProfile
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, Http404

from django.views.generic import TemplateView, UpdateView


class ProfileHomepageView(TemplateView):
    model = User
    template_name = "profiles/profile_home.html"

class ProfileUpdateView(UpdateView):
    model = User
    template_name = "profiles/update_form.html"
