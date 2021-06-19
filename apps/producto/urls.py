from django.urls import path
from .views import obtenerProductos, agregarProducto

urlpatterns = [
    path('', obtenerProductos, name= 'inicioProductos'),
    path('nuevo-producto/', agregarProducto, name= 'nuevoProducto'),
]