from django.shortcuts import render, redirect
from .forms import RegistroUsuario, IniciarSesion
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def registro(request):
    formulario = None
    if request.method == 'POST':
        formulario = RegistroUsuario(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.refresh_from_db()
            usuario.perfil.rut = formulario.cleaned_data.get('rut')
            usuario.save()
            return redirect('principal')
    if request.method == 'GET':
        formulario = RegistroUsuario()
    contexto = {
        'formulario': formulario
    }
    return render(request, 'cuentas/registro.html', context=contexto)


def iniciarSesion(request):
    formulario = None
    if request.method == 'GET':
        formulario = IniciarSesion(request)
    if request.method == 'POST':
        usuario = request.POST.get('username')
        contrasena = request.POST.get('password')
        usuario = authenticate(username=usuario, password=contrasena)
        if usuario is not None:
            login(request, usuario)
            return redirect('principal')
    contexto = {
        'formulario': formulario
    }
    return render(request, 'cuentas/iniciarSesion2.html', context=contexto)


def salir(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('principal')
