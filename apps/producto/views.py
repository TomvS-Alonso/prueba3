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

def editarProducto(request, idProducto):
    producto = None
    try:
        producto = Producto.objects.get(pk= idProducto)
    except ObjectDoesNotExist as e:
        pass
    if producto == None:
        return redirect('inicioProductos')
    formulario = None
    if request.method == 'GET':
        formulario = FormularioProducto(instance = producto)
    if request.method == 'POST':
        formulario = FormularioProducto(data = request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicioProductos')
        else:
            formulario = FormularioProducto(instance = producto)
    contexto = {
        'ruta':'producto',
        'formulario': formulario
            }
    return render(request,'producto/editarProducto.html',context=contexto)