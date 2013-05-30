from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

admin.autodiscover()

from . import views
from movies.views import MovieListView
from djangoratings.views import AddRatingFromModel

from profiles.views import *

urlpatterns = patterns('',
    url(r'^$', views.HomepageView.as_view(), name='home'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^movies/', include('movies.urls', namespace='movies')),
    url(r'^all/$', MovieListView.as_view(), name='list'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include('profiles.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/settings/core/$', UserUpdateView.as_view(), name='user_update'),
    url(r'^accounts/settings/info/$', UserProfileUpdateView.as_view(), name='userprofile_update'),
)

urlpatterns += patterns('',
        url(r'ratings/(?P<object_id>\d+)/(?P<score>\d+)/', login_required(AddRatingFromModel()), {
            'app_label': 'movies',
            'model': 'movie',
            'field_name': 'user_rating',
    }),
)

