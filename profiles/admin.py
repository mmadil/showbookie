from django.contrib import admin
from profiles.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user',)

admin.site.register(UserProfile, UserProfileAdmin)

