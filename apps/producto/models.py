from django.db import models
from apps.categoria.models import Categoria

# Create your models here.
class Producto(models.Model):
    nombre_producto = models.CharField('Nombre del producto', max_length= 50, blank= False, null= False)
    descripcion_producto = models.CharField('descripcion del producto', max_length= 150, blank= False, null= False)
    precio_producto = models.IntegerField('Precio del producto', blank=False, null= False)
    fecha_ingreso = models.DateTimeField('Fecha de creacion Del recordatorio', auto_now= True)
    
    # Union con categoria ( Sujeto a combio.. )
    categoria_producto = models.ForeignKey(Categoria, on_delete= models.SET_NULL, null= True)
    
    estado_producto = models.CharField('Estado del Producto', max_length= 50, blank= False, null= False)
    stock_producto = models.SmallIntegerField('Stock del producto', blank=False, null= False)

    def __str__(self):
        return self.nombre_producto