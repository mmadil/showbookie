from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.comments.models import Comment

from reviews.models import UserExperience

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, Http404

from django.views.generic import TemplateView, UpdateView

from .forms import ProfileUpdateForm

class ProfileHomepageView(TemplateView):
    model = User
    template_name = "profiles/profile_home.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileHomepageView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username = self.request.user.username)
        context['comment_count'] = Comment.objects.all().filter(user=user).count()
        context['comments'] = Comment.objects.all().filter(user=user).order_by('-submit_date')[:5]
        return context


class ProfileUpdateView(UpdateView):
    form_class = ProfileUpdateForm
    model = User
    fields = ['firstname','lastname','email']
    template_name = "profiles/profile_update.html"



