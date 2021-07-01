from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Producto
from apps.categoria.models import Categoria
from .forms import FormularioProducto
from apps.personas.models import Perfil
from apps.carro.models import Carrito
# Create your views here.


def obtenerProductos(request):
    productos = Producto.objects.all()
    contexto = {
        'ruta': 'producto',
        'productos': productos
    }
    return render(request, 'producto/inicioProducto.html', context=contexto)


def agregarProducto(request):
    formulario = None
    if request.method == 'GET':
        formulario = FormularioProducto()
    elif request.method == 'POST':
        formulario = FormularioProducto(request.POST, request.FILES)
        formulario.save()
        return redirect('inicioProductos')
    contexto = {
        'ruta': 'producto',
        'formulario': formulario
    }
    return render(request, 'producto/nuevoProducto.html', context=contexto)


def editarProducto(request, idProducto):
    producto = None
    try:
        producto = Producto.objects.get(pk=idProducto)
    except ObjectDoesNotExist as e:
        pass
    if producto == None:
        return redirect('inicioProductos')
    formulario = None
    if request.method == 'GET':
        formulario = FormularioProducto(instance=producto)
    if request.method == 'POST':
        formulario = FormularioProducto(
            request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicioProductos')
        else:
            formulario = FormularioProducto(instance=producto)
    contexto = {
        'ruta': 'producto',
        'formulario': formulario
    }
    return render(request, 'producto/editarProducto.html', context=contexto)


def eliminarProducto(request, idProducto):
    try:
        productoEncontrado = Producto.objects.get(pk=idProducto)
        productoEncontrado.delete()
    except ObjectDoesNotExist:
        pass
    return redirect('inicioProductos')


def producto(request):
    productoEncontrado = Producto.objects.all()
    categoriaEncontrada = Categoria.objects.all()

    contexto = {
        'productos': productoEncontrado,
        'categorias': categoriaEncontrada
    }
    return render(request, 'producto/productos.html', contexto)


def filtro(request, idCategoria):
    productoEncontrado = Producto.objects.filter(
        categoria_producto_id=idCategoria)
    categoriaEncontrada = Categoria.objects.all()

    contexto = {
        'productos': productoEncontrado,
        'categorias': categoriaEncontrada
    }
    return render(request, 'producto/productos.html', contexto)


def agregarCarrito(request, idProducto):
    productoCarrito = Carrito.objects.create(
        usuario=Perfil.objects.get(usuario=request.user.id),
        producto=Producto.objects.get(id=idProducto))
    return redirect('producto')


def eliminarCarrito(request, idProducto):
    productoCarrito = Carrito.objects.delete(
        producto=Producto.objects.get(id=idProducto))
