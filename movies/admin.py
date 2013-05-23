from django.contrib import admin
from .models import Timing, Movie

class MovieAdmin(admin.ModelAdmin):
    date_hierarchy = "start_date"
    fields = ('title', 'slug', 'photo', 'description', 'start_date', 'end_date', 'timings', 'published', 'enable_comments')
    list_display = ['published', 'title', 'start_date', 'end_date']
    list_display_links = ['title']
    list_editable = ['published',]
    list_filter = ['published']
    prepopulated_fields = {'slug': ['title',]}
    search_fields = ['title', 'description']

class TimingAdmin(admin.ModelAdmin):
    fields = ('time',)
    list_display = ['time']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Timing, TimingAdmin)
