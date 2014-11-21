from django.http import Http404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from forms import ReservaForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from models import Reserva, Objecte




def index(request):
    list_ult_reserves = Reserva.objects.all().order_by('data_inici')
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

@login_required
def espai_usuari(request):

    llista_pendent =  Reserva.objects.all().filter(user__id__icontains=request.user.id).filter(objecte__disponible__icontains='No')
    llista_tornades = Reserva.objects.filter(user__id__icontains=request.user.id).filter(objecte__disponible__icontains='Si')
    return render(request, 'reserves/espai_usuari.html', {'llista_pendent': llista_pendent, 'llista_tornades': llista_tornades,'nomuser': request.user.username})

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/reserves")

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
                    return espai_usuari(request)
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
@login_required
def nueva_reserva(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = ReservaForm(request.POST)


        if formulario.is_valid():
            id = request.POST['objecte']
            obj=Objecte.objects.get(pk=id)
            obj.disponible = 'No'
            obj.save()
            formulario.save()
            return espai_usuari(request)
        else:
            messages.error(request, "Error")
    else:
        formulario = ReservaForm()
        formulario.fields['objecte'].queryset = Objecte.objects.filter(disponible='Si')
        messages.error(request, "Error")

    return render(request, 'reserves/nueva_reserva.html', {'formulario': formulario, 'usuario':usuario})

def retornar(request, objecte_id):

    obj = Objecte.objects.get(pk=objecte_id)
    obj.disponible = 'Si'
    obj.save()
    accio = "Reserva Retornada Correctament"
    return espai_usuari(request)

def eliminar(request, reserva_id):

    res = Reserva.objects.get(pk=reserva_id)
    res.delete()
    accio = "Reserva Eliminada Correctament"
    return espai_usuari(request)

def events(request, accio):
    pass