from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, default='')
    facebook = models.CharField('Facebook Username', max_length=30, blank=True, default='')
    twitter = models.CharField('Twitter Username', max_length=30, blank=True, default='')

    def __unicode__(self):
        return self.user.username

