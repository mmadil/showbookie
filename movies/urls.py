from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^(?P<slug>[\w-]+)/$', views.MovieDetailView.as_view(), name='detail'),
    url(r'^all/$', views.MovieListView.as_view(), name='list'),
)
