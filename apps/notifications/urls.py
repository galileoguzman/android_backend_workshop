# urls.py
from django.conf.urls import include, url

from views import *

urlpatterns = [
    url(r'^notifications/$', notification_new, name='notification_new'),
]