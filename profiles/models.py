from django.contrib.auth.models import User
from django.db import models
    
from django.dispatch import receiver
from guardian.shortcuts import assign_perm
from registration.signals import user_registered

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, default='')
    facebook = models.CharField('Facebook Username', max_length=30, blank=True, default='')
    twitter = models.CharField('Twitter Username', max_length=30, blank=True, default='')

    def __unicode__(self):
        return self.user.username


def createUserProfile(sender, user, request, **kwargs):
	user_profile = UserProfile.objects.create(user=user)
	from guardian.shortcuts import assign_perm

	assign_perm('change_userprofile', user, user_profile)
	assign_perm('delete_userprofile', user, user_profile)
	assign_perm('change_user', user, user)

user_registered.connect(createUserProfile)

