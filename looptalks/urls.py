from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin


from apps.movies import urls as movies_urls
from apps.users import urls as users_urls
from apps.notifications import urls as notifications_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(movies_urls)),
    url(r'^', include(notifications_urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
