from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField('Ingrese su RUT ', max_length=12,
                           null=False, blank=False, unique=True)
    fecha_creacion = models.DateField(auto_now=True)
<<<<<<< HEAD
    admin = models.BooleanField(default=False)
=======
>>>>>>> 0881992825f0e7e4a3277a4908d74b960c85ca89

    def __str__(self):
        return self.usuario.username


@receiver(post_save, sender=User)
def actualizar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
    instance.perfil.save()
