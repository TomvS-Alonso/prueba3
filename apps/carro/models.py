from apps.producto.models import Producto
from apps.personas.models import Perfil
from django.db import models

# Create your models here.


class Carrito (models.Model):
    # usuario
    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    # producto
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    # cantidad a comprar
    cantidad = models.PositiveIntegerField(blank=False, default=1, null=False)
