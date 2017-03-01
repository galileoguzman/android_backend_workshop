# urls.py
from django.conf.urls import include, url

from views import *

urlpatterns = [
    url(r'^$', home, name='home'),
]