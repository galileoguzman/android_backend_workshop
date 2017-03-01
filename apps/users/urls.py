# urls.py
from django.conf.urls import include, url

from views import *

urlpatterns = [
    # LOGIN MANAGER
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
]