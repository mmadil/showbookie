from movies.models import Movie

def all_movies(request):
    movies = Movie.objects.all()[:5]

    return {
        'all_movies': movies
    }
