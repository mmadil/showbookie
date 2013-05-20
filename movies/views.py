from .models import Movie
from django.views.generic import DetailView

class PublishedPostMixin(object):
    def get_queryset(self):
        queryset = super(PublishedPostMixin).get_queryset()
        return queryset.filter(published=True)

class MovieDetailView(DetailView):
    model = Movie
