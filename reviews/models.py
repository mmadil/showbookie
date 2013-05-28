from django.db import models
from movies.models import Movie
from django.contrib.comments.models import Comment

class UserExperience(Comment):
    movie = models.ForeignKey(Movie)
    experience = models.CharField('User Experience', max_length=20)

#    def __unicode__(self):
#        return self.user
