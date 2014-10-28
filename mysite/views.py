from django.http import HttpResponse
from django.conf import settings


def index(request):
    return HttpResponse("Hello, world. You're at HOME index.")
if settings.DEBUG and settings.STATIC_ROOT:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'),
            'django.views.static.serve',
            {'document_root' : settings.STATIC_ROOT }),)
