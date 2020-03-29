from django.urls import include, path

from .views import Registro

urlpatterns = [
    path('registro/', Registro.as_view(), name='registroUsuario'),
]

