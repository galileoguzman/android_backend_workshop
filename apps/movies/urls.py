# urls.py
from django.conf.urls import include, url

from views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^new/$', movie_new, name='movie_new'),
    url(r'^edit/(?P<id>\d+)/$', movie_edit, {}, 'movie_edit'),
    url(r'^delete/(?P<id>\d+)/$', movie_delete, name='opinion_delete'),
]