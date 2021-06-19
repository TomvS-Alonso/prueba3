from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Producto
from .forms import FormularioProducto
# Create your views here.

def obtenerProductos(request):
    productos = Producto.objects.all()
    contexto = {
        'ruta':'producto',
        'productos':productos
    }
    return render(request, 'producto/inicioProducto.html', context= contexto)

def agregarProducto(request):
    formulario = None
    if request.method == 'GET':
        formulario = FormularioProducto()
    elif request.method == 'POST':
        formulario = FormularioProducto(request.POST)
        formulario.save()
        return redirect('inicioProductos')
    contexto = {
        'ruta': 'producto',
        'formulario': formulario
    }        
    return render(request, 'producto/nuevoProducto.html', context= contexto)

