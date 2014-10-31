from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
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

def espai_usuari(request, usuari):
    list_ult_reserves = Reserva.objects.all().order_by('data_inici')

def ingresar(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return index(request)
                else:
                    return render(request, 'reserves/no_actiu.html')
            else:
                return render(request, 'reserves/no_usuari.html')
    else:
        formulario = AuthenticationForm
        return render(request, 'reserves/ingresar.html', {'formulario': formulario})

def signup(request):
    if(request.method == 'POST'):
        formulario= UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render(request, 'reserves/signup.html', {'formulario': formulario})


