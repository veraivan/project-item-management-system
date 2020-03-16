"""
ESTE ARCHIVO DE URL TIENE LOS LOS PARAMENTROS PARA LOS ARCHIVOS DE STATIC PARA HACER DEPLOYMENT DEL PROYECTO
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf .urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loginAuth.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
