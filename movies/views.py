from .models import Movie
from django.views.generic import DetailView, ListView

class PublishedPostMixin(object):
    def get_queryset(self):
        queryset = super(PublishedPostMixin).get_queryset()
        return queryset.filter(published=True)

class MovieDetailView(DetailView):
    model = Movie



class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'

