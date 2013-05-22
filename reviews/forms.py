from django import forms
from django.contrib.comments.forms import CommentForm
from .models import CustomCommentManager

class CustomCommentFormManager(CommentForm):
    experience = forms.CharField(max_length=20)

    def get_comment_model(self):
        return CustomCommentManager

    def get_comment_create_data(self):
        data = super(CustomCommentFormManager, self).get_comment_create_data()
        data['title'] = self.cleaned_data['title']
        return data
