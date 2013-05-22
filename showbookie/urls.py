from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

from . import views

urlpatterns = patterns('',
    url(r'^$', views.HomepageView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/profile/', include('profiles.urls', namespace='profiles')),
    url(r'^movies/', include('movies.urls', namespace='movies')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
