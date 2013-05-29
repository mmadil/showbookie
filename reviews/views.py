from movies.models import Movie

def CommentView(request):
    allComments = UserExperience.objects.all().filter(id=movie.id)
    paginator = Paginator(comments, 10)
    comment = paginator.page(1)
