from django.shortcuts import render, redirect
from .forms import RegistroUsuario, IniciarSesion
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
            messages.success(request, 'Usuario {} registrado con éxito'.format(
                username
            ))
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
            messages.info(request, 'Bienvenido {}'.format(usuario))
            login(request, usuario)
            return redirect('principal')

        else:
            messages.info(request, 'Usuario o contraseña no son correctos')
    contexto = {
        'formulario': formulario
    }
    return render(request, 'cuentas/iniciarSesion2.html', context=contexto)


def salir(request):
    if request.user.is_authenticated:
        messages.info(request,'Adios :c, vuelva pronto')
        logout(request)
    return redirect('principal')
