from django.shortcuts import render, redirect
from .forms import RegistroUsuario, IniciarSesion
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.contrib import messages
=======
>>>>>>> 0881992825f0e7e4a3277a4908d74b960c85ca89
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
<<<<<<< HEAD
            messages.success(request, 'Usuario {} registrado con éxito'.format(
                username
            ))
=======
>>>>>>> 0881992825f0e7e4a3277a4908d74b960c85ca89
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
<<<<<<< HEAD
            messages.info(request, 'Bienvenido {}'.format(usuario))
            login(request, usuario)
            return redirect('principal')

        else:
            messages.info(request, 'Usuario o contraseña no son correctos')
=======
            login(request, usuario)
            return redirect('principal')
>>>>>>> 0881992825f0e7e4a3277a4908d74b960c85ca89
    contexto = {
        'formulario': formulario
    }
    return render(request, 'cuentas/iniciarSesion2.html', context=contexto)


def salir(request):
    if request.user.is_authenticated:
<<<<<<< HEAD
        messages.info(request,'Adios :c, vuelva pronto')
=======
>>>>>>> 0881992825f0e7e4a3277a4908d74b960c85ca89
        logout(request)
    return redirect('principal')
