from django.contrib import admin
from .models import UserExperience
from django.contrib.comments.models import Comment

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserExperience, CommentAdmin)
admin.site.register(Comment)
