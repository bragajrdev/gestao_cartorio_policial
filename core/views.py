from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404
from datetime import datetime, timedelta
# Create your views here.

#def index(request):
#     return redirect('/cartorio/')

def login_user(request):
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect ('/')
        else:
            messages.error(request, "Usuário ou senha inválido!")
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request,'cartorio.html', dados)

@login_required(login_url='/login/')
def evento(request):
    id_evento=request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        procedimento = request.POST.get('procedimento')
        tipo = request.POST.get('tipo')
        investigado = request.POST.get('investigado')
        vitima = request.POST.get('vitima')
        fato = request.POST.get('fato')
        autos= request.POST.get('autos')
        data_instauracao=request.POST.get('data_instauracao')
        data_remessa = request.POST.get('data_remessa')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.procedimento = procedimento
                evento.tipo = tipo
                evento.investigado = investigado
                evento.vitima = vitima
                evento.fato = fato
                evento.autos = autos
                evento.data_instauracao = data_instauracao
                evento.data_remessa = data_remessa
                evento.save()
            # Evento.objects.filter(id=id_evento).update(titulo=titulo,
            #                                            data_evento=data_evento,
            #                                            descricao=descricao)
        else:
            Evento.objects.create(procedimento=procedimento,
                                  tipo=tipo,
                                  investigado=investigado,
                                  vitima=vitima,
                                  fato=fato,
                                  autos=autos,
                                  data_instauracao=data_instauracao,
                                  data_remessa=data_remessa,
                                  usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario=request.user
    try:
        evento= Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')
