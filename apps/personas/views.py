from django.shortcuts import render, redirect
from .forms import RegistroUsuario, IniciarSesion
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
