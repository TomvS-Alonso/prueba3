from django.urls import path
from .views import principal, vistaNintendo, vistaPlay, vistaXbox, vistaPc, vistaComponentes, vistaCarro

urlpatterns = [
    path('', principal, name='principal'),
    path('/nintendo', vistaNintendo, name='nintendo'),
    path('/playstation', vistaPlay, name='playstation'),
    path('/xbox', vistaXbox, name='Xbox'),
    path('/pc-armados', vistaPc, name='pc'),
    path('/pc-componentes', vistaComponentes, name='componentes'),
    path('/carro', vistaCarro, name='carro')
]
