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
    return render(request, 'carrito/carro.html')

def vistaSearch(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        searched = searched
        product = Producto.objects.filter(nombre_producto__contains=searched)
        return render(request, 'buscar/search.html',
        {'searched': searched,
        'product':product})
    else:
        return render(request, 'buscar/search.html')
