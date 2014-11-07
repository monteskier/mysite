from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('reserves.urls')),
    url(r'^index$', include('reserves.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reserves/', include('reserves.urls')),
)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
