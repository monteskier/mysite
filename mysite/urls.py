from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('home.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reserves/', include('reserves.urls')),
    url(r'^home/', include('home.urls'))
)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
