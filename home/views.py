from django.shortcuts import render_to_response

def index(request):
    hora = "tot be"
    return render_to_response('home/index.html',
    {'fechahora_actual': hora})
