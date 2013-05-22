from .models import UserProfile
from django.contrib.auth.models import User

from django.views.generic import TemplateView

class ProfileHomepageView(TemplateView):
    model = UserProfile, User
    template_name = "profiles/profile_home.html"
