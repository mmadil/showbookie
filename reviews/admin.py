from django.contrib import admin
from .models import UserExperience

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserExperience, CommentAdmin)
