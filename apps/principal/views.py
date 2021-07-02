from django.shortcuts import render
from apps.producto.models import Producto
# Create your views here.


def principal(request):
    return render(request, 'base/principal.html')


def vistaNintendo(request):
    return render(request, 'consolas/nintendo/nintendo.html')


def vistaPlay(request):
    return render(request, 'consolas/ps4/ps4.html')


def vistaXbox(request):
    return render(request, 'consolas/xbox/xbox.html')


def vistaPc(request):
    return render(request, 'pc/armados/armados.html')


def vistaComponentes(request):
    return render(request, 'pc/componentes/componentes.html')


def vistaCarro(request):
<<<<<<< HEAD
    return render(request, 'carrito/carro.html')

def contacto(request):
    return render(request, 'base/contacto.html')

def vistaSearch(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        searched = searched
        product = Producto.objects.filter(nombre_producto__icontains=searched)
        return render(request, 'buscar/search.html',
        {'searched': searched,
        'product':product})
    else:
        return render(request, 'buscar/search.html')
=======
    return render(request, 'carro/carro.html')
>>>>>>> 0881992825f0e7e4a3277a4908d74b960c85ca89
