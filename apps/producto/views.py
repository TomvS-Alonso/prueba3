from apps.personas.models import Perfil
from apps.carro.models import Carrito
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Producto
# Create your views here.


def obtenerProductos(request):
    productos = Producto.objects.all()
    contexto = {
        'ruta': 'producto',
        'productos': productos
    }
    return render(request, 'producto/inicioProducto.html', context=contexto)


def agregarCarrito(request, idProducto):
    productoCarrito = Carrito.objects.create(
        usuario=Perfil.objects.get(usuario=request.user.id),
        producto=Producto.objects.get(id=idProducto))
    return redirect('producto')
