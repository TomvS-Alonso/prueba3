from django.urls import path
from .views import registro, iniciarSesion, salir

urlpatterns = [
    path('registro/', registro, name='Registro'),
    path('salir/', salir, name='salir'),
    path('iniciar-sesion/', iniciarSesion, name='iniciar_sesion')
]
