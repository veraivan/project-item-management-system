from django.urls import include, path
from django.conf.urls import url
from .views import Registro, dashboard, logout, loggin,EditarDatosUsuario

urlpatterns = [
    path('', loggin, name='account_loggin'),
    path('dashboard/', dashboard, name='account_dashboard'),
    path('logout/', logout, name='account_logout'),
    path('registro/', Registro.as_view(), name='registroUsuario'),
    url(r'^editar/(?P<id_usuario>\d+)/$',EditarDatosUsuario.as_view(), name='editar_dato'),
]

