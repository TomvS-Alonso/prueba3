from django.urls import path
<<<<<<< HEAD
from .views import principal, vistaNintendo, vistaPlay, vistaXbox, vistaPc, vistaComponentes, vistaCarro, vistaSearch, contacto
=======
from .views import principal, vistaNintendo, vistaPlay, vistaXbox, vistaPc, vistaComponentes, vistaCarro
>>>>>>> 0881992825f0e7e4a3277a4908d74b960c85ca89

urlpatterns = [
    path('', principal, name='principal'),
    path('nintendo', vistaNintendo, name='nintendo'),
    path('playstation', vistaPlay, name='playstation'),
    path('xbox', vistaXbox, name='Xbox'),
    path('pc-armados', vistaPc, name='pc'),
    path('pc-componentes', vistaComponentes, name='componentes'),
<<<<<<< HEAD
    # path('carro/', vistaCarro, name='Carrito'),
    path('buscar', vistaSearch, name='search'),
    path('contacto/', contacto, name='Nosotros'),
=======
    path('carro', vistaCarro, name='carro')
>>>>>>> 0881992825f0e7e4a3277a4908d74b960c85ca89
]
