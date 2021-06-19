from django.urls import path
from .views import obtenerCategoria, agregarCategoria

urlpatterns = [
    path('', obtenerCategoria, name= 'inicioCategoria'),
    path('nueva-categoria/', agregarCategoria, name= 'nuevaCategoria'),
]