from django.urls import path
from .views import obtenerCategoria, agregarCategoria, editarCategoria, eliminarCategoria

urlpatterns = [
    path('', obtenerCategoria, name= 'inicioCategoria'),
    path('nueva-categoria/', agregarCategoria, name= 'nuevaCategoria'),
    path('editar-categoria/<int:idCategoria>', editarCategoria, name='modificarCategoria' ),
    path('eliminar-categoria/<int:idCategoria>', eliminarCategoria, name= 'eliminarCategoria')
]