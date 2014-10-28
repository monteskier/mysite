from django.http import Http404
from django.shortcuts import render

from reserves.models import Reserva
def index(request):
    list_ult_reserves = Reserva.objects.all().order_by('data_inici')[:5]
    context = {'list_ult_reserves': list_ult_reserves}
    return render(request, 'reserves/index.html', context)

def detail(request,  reserva_id):
    try:
        reserva = Reserva.objects.get(pk=reserva_id)
    except Reserva.DoesNotExist:
        raise Http404
    return render(request, 'reserves/detail.html', {'reserva': reserva})
def actReserva(request):
    pass
