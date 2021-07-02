from django.urls import path
from .views import principal, contacto

urlpatterns = [
    path('',principal, name='principal'),
    path('contacto/', contacto, name='Nosotros')
]