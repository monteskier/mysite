from django.conf.urls import patterns, url
from reserves import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<reserva_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<reserva_id>\d+)/actReserva/$', views.actReserva, name='actReserva'),
)

