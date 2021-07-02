from django.shortcuts import render, redirect
from apps.personas.models import Perfil
from apps.carro.models import Carrito
from django.contrib.auth.models import User
from apps.producto.models import Producto
from apps.categoria.models import Categoria

# Create your views here.

def carrito(request):
    total = 0

    perfil = Perfil.objects.get(usuario = User.objects.get(id = request.user.id))
    productos = Carrito.objects.filter(usuario = perfil.id)
    for producto in productos:
        total = total + producto.producto.precio_producto
    context = {
        'productos': productos,
        'perfil': perfil,
        'total': total
    }
    return render(request, 'carrito/carro.html', context)

def agregarCarrito(request, idProducto):
    productoCarrito = Carrito.objects.create(
        usuario=Perfil.objects.get(usuario=request.user.id),
        producto=Producto.objects.get(id=idProducto))
    return redirect('productos')


def eliminarCarrito(request, idProducto):
    productoCarrito = Carrito.objects.get(id=idProducto)
    productoCarrito.delete()
    return redirect('Carrito')
    