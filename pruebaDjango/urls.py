"""pruebaDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.principal.urls')),
    path('producto/', include('apps.producto.urls')),
    path('categoria/', include('apps.categoria.urls')),
    path('cuentas/', include('apps.personas.urls')),
<<<<<<< HEAD
    path('carro/', include('apps.carro.urls')),
=======
>>>>>>> 0881992825f0e7e4a3277a4908d74b960c85ca89

] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
