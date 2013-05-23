from django.db import models
from django.contrib.comments.models import Comment

from movies.models import Movie

class UserExperience(Comment):
    experience = models.CharField('User Experience', max_length=20)

    def __unicode__(self):
        return self.user.username
