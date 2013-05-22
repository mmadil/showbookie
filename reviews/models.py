from django.db import models
from django.contrib.comments.models import Comment

class CustomCommentManager(Comment):
    experience = models.CharField('User Experience', max_length=20)
