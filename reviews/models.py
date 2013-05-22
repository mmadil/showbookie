from django.db import models
from django.contrib.comments.models import Comment

class UserExperience(Comment):
    experience = models.CharField('User Experience', max_length=20)
