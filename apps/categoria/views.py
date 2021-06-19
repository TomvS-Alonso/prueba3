from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Categoria
from .forms import FormularioCategria # CREAR

# Create your views here.
def obtenerCategoria(request):
    categorias = Categoria.objects.all()
    contexto = {
        'ruta': 'categoria',
        'categorias': categorias
    }
    return render(request, 'categoria/inicioCategoria.html', context= contexto)

def agregarCategoria(request):
    formulario = None
    if request.method == 'GET':
        formulario = FormularioCategria()
    elif request.method == 'POST':
        formulario = FormularioCategria(request.POST)
        formulario.save()
        return redirect('inicioCategoria')
    contexto = {
        'ruta': 'categoria',
        'formulario': formulario
    }
    return render(request, 'categoria/nuevaCategoria.html', context= contexto)