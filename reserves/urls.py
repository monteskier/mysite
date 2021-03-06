from django.conf.urls import patterns, url
from reserves import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^nueva_reserva/$', views.nueva_reserva, name='nueva_reserva'),
    url(r'^(?P<reserva_id>\d+)/$', views.detail, name='detail'),
    url(r'^retornar/(?P<objecte_id>\d+)/$', views.retornar, name='retornar'),
    url(r'^eliminar/(?P<reserva_id>\d+)/$', views.eliminar, name='eliminar'),
    url(r'^espai_usuari/$', views.espai_usuari, name='espai_usuari'),
    url(r'^(?P<reserva_id>\d+)/actReserva/$', views.actReserva, name='actReserva'),
)

