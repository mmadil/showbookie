from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'$', views.ProfileHomepageView.as_view(), name='home'),
)
