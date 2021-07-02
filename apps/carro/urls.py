from django.urls import path
from apps.principal.views import vistaCarro
from .views import carrito, agregarCarrito, eliminarCarrito

urlpatterns = [
    path('', carrito, name='Carrito'),
    path('carrito-agregar/<int:idProducto>', agregarCarrito, name='agregarCarro'),
    path('carrito-eliminar/<int:idProducto>', eliminarCarrito, name='eliminarCarro')
]
