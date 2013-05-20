from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

from . import views

urlpatterns = patterns('',
    url(r'^$', views.HomepageView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('movies.urls', namespace='movie')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
