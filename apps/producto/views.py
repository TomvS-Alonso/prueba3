from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Producto
# Create your views here.

def obtenerProductos(request):
    productos = Producto.objects.all()
    contexto = {
        'ruta':'producto',
        'productos':productos
    }
    return render(request, 'producto/inicioProducto.html', context= contexto)

