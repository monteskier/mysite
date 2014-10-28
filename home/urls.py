from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)+static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
