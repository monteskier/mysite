from django.conf.urls import patterns, url
from reserves import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^logout/$', views.logout_view(), name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^(?P<reserva_id>\d+)/$', views.detail, name='detail'),
    url(r'^espai_usuari/$', views.espai_usuari, name='espai_usuari'),
    url(r'^(?P<reserva_id>\d+)/actReserva/$', views.actReserva, name='actReserva'),
)

