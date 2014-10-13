from reserves.models import Objecte, Reserva, Tipus, Interessat, Salas
from django.contrib import admin


class ReservaAdmin(admin.ModelAdmin):
    list_display = ('objecte', 'interessat', 'sala', 'data_inici', 'data_final', 'demanat_avui')


admin.site.register(Objecte)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Tipus)
admin.site.register(Interessat)
admin.site.register(Salas)



