from django.urls import path
from .views import obtenerProductos, agregarProducto, editarProducto, eliminarProducto

urlpatterns = [
    path('', obtenerProductos, name= 'inicioProductos'),
    path('nuevo-producto/', agregarProducto, name= 'nuevoProducto'),
    path('editar-producto/<int:idProducto>', editarProducto, name='modificarProducto'),
    path('eliminar-producto/<int:idProducto>', eliminarProducto, name= 'eliminar')
]