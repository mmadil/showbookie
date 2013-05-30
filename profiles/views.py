from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.comments.models import Comment

from reviews.models import UserExperience

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404

from django.views.generic import DetailView, TemplateView, UpdateView, RedirectView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .forms import *

def user_redirect_view(request, username):
    user = get_object_or_404(User, username=username)
    return HttpResponseRedirect(reverse('user_info', kwargs={'username': user.username}))


class UserInfoView(DetailView):
    context_object_name = 'userinfo'
    template_name = 'profiles/user_detail.html'
    model = User

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return user

    def get_context_data(self, **kwargs):
        context = super(UserInfoView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])
        userprofile = get_object_or_404(UserProfile, user=user)
        context['userprofile'] = userprofile
        context['comment_count'] = Comment.objects.all().filter(user=user).count()
        context['comments'] = Comment.objects.all().filter(user=user).order_by('-submit_date')[:5]
        return context


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "profiles/user_update.html"
    permission_required = "auth.change_user"

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, "Your account settings have been saved")
        return reverse_lazy("user_update")

class UserProfileUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = UserProfileUpdateForm
    model = UserProfile
    template_name = "profiles/userprofile_update.html"
    permission_required = "profiles.change_userprofile"

    def get_object(self):
        return self.request.user.userprofile

    def get_success_url(self):
        message.success(self.request, "Your profile settings have been saved")
        return reverse_lazy("userprofile_update")

class MyProfileView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        return reverse('user_detail', kwargs={'username':user.username})
