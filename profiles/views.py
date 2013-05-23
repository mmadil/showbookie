from .models import UserProfile
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, Http404

from django.views.generic import TemplateView


class ProfileHomepageView(TemplateView):
    context_object_name = 'userinfo'
    model = User
    template_name = "profiles/profile_home.html"
