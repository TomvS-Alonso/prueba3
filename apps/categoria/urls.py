from django.urls import path
from .views import obtenerCategoria, agregarCategoria, editarCategoria

urlpatterns = [
    path('', obtenerCategoria, name= 'inicioCategoria'),
    path('nueva-categoria/', agregarCategoria, name= 'nuevaCategoria'),
    path('editar-categoria/<int:idCategoria>', editarCategoria, name='modificarCategoria' )
]