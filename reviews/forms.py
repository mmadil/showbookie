from django import forms
from .models import UserExperience
from django.contrib.comments.forms import CommentForm

from movies.models import Movie
from django.contrib.comments.moderation import CommentModerator, moderator


class UserExperienceForm(CommentForm):
    experience = forms.CharField(max_length=20)

    def get_comment_model(self):
        return UserExperience

    def get_comment_create_data(self):
        data = super(UserExperienceForm, self).get_comment_create_data()
        data['experience'] = self.cleaned_data['experience']
        data['movie_id'] = self.cleaned_data['object_pk']
        return data

class MovieCommentModerator(CommentModerator):
        email_notification = False
        auto_close_field = "start_date"
        close_after = 31

moderator.register(Movie, MovieCommentModerator)

