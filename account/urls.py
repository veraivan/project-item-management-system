from django.urls import include, path

from django.conf.urls import url
from .views import Registro, dashboard, logout, loggin,EditarDatosUsuario,VerDatos


from .views import *


urlpatterns = [
    path('', loggin, name='account_loggin'),
    path('dashboard/', dashboard, name='account_dashboard'),
    path('logout/', logout, name='account_logout'),
    url(r'^editar/(?P<id_usuario>\d+)/$',EditarDatosUsuario.as_view(), name='editar_dato'),
    path('ver/<int:pk>/', VerDatos.as_view(), name='ver_dato'),
    path('registro/', Registro.as_view(), name='account_registro'),
    path('roles/', UserRolList.as_view(), name='account_role_list'),
    path('roles/crear/', UserRolCreate.as_view(), name='account_role_create'),
    path('roles/<int:id>/', UserRolDetail.as_view(), name='account_role_detail'),
    path('roles/<int:id>/editar/', UserRolUpdate.as_view(), name='account_role_update'),
    path('roles/<int:id>/eliminar/', UserRolDelete.as_view(), name='account_role_delete'),
    path('roles/<int:id>/asignar/', UserRolAssign.as_view(), name='account_role_assign'),
    path('roles/<int:id>/quitar/', UserRolRemove.as_view(), name='account_role_remove'),

]

