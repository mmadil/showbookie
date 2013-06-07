import datetime
from django.shortcuts import render

from movies.models import Movie


def IndexView(request):
	now_showing = Movie.objects.exclude(end_date__lte=datetime.date.today())[:5]
	popular = Movie.objects.all().order_by('-user_rating_score')[:5]
	return render(request,'index.html',{'now_showing':now_showing, 'popular':popular})