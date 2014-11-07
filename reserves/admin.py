from reserves.models import Objecte, Reserva, Tipus, Salas
from django.contrib import admin


class ReservaAdmin(admin.ModelAdmin):
    list_display = ('objecte', 'user', 'sala', 'data_inici', 'data_final', 'demanat_avui')


admin.site.register(Objecte)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Tipus)
admin.site.register(Salas)



