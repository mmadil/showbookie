from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
    url(r'^$', MyProfileView.as_view(), name='my_profile'),
    url(r'^(?P<username>[\w-]+)/$', user_redirect_view, name='user_detail'),
    url(r'^(?P<username>\w+)/info/$', UserInfoView.as_view(), name='user_info'),
)
