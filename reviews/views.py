from .models import UserExperience
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def listing(request):
    review_list = UserExperience.objects.all()
    paginator = Paginator(review_list, 4)

    page = request.GET('page')
    try:
        paginated_reviews = paginator.page(page)
    except PageNotAnInteger:
        paginated_reviews = paginator.page(1)
    except EmptyPage:
        paginated_reviews = paginator.page(paginator.num_pages)

    return render_to_response('forms.html', { 'reviews_': paginated_reviews })
