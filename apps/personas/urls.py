from django.urls import path
from .views import registro

urlpatterns = [
    path('registro/', registro, name='Registro'),
    # path('salir/', )
]
