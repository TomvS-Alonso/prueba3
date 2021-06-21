from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Categoria
from .forms import FormularioCategoria # CREAR

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
        formulario = FormularioCategoria()
    elif request.method == 'POST':
        formulario = FormularioCategoria(request.POST)
        formulario.save()
        return redirect('inicioCategoria')
    contexto = {
        'ruta': 'categoria',
        'formulario': formulario
    }
    return render(request, 'categoria/nuevaCategoria.html', context= contexto)

def editarCategoria(request, idCategoria):
    categoria = None
    try:
        categoria = Categoria.objects.get(pk= idCategoria)
    except ObjectDoesNotExist:
        pass
    if categoria == None:
        return redirect('inicioCategoria')
    formulario = None
    if request.method == 'GET':
        formulario = FormularioCategoria(instance= categoria)
    if request.method == 'POST':
        formulario = FormularioCategoria(data= request.POST, instance= categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicioCategoria')
        else:
            formulario = FormularioCategoria(instance= categoria)
    contexto = {
        'ruta': 'categoria',
        'formulario': formulario
    }
    return render(request, 'categoria/editarCategoria.html', context= contexto)