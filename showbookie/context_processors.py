from movies.models import Movie

def this_week(request):
    all_movies = Movie.objects.all()
    start_date = all_movies.get().start_date
    end_date = all_movies.get().end_date


    return {
        'all_movies': all_movies
    }
