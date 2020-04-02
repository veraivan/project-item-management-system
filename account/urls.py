from django.urls import include, path

from .views import *

urlpatterns = [
    path('', loggin, name='account_loggin'),
    path('dashboard/', dashboard, name='account_dashboard'),
    path('logout/', logout, name='account_logout'),
    path('registro/', Registro.as_view(), name='account_registro'),
    path('roles/', UserRolList.as_view(), name='account_role_list'),
    path('roles/crear/', UserRolCreate.as_view(), name='account_role_create'),
    path('roles/<int:id>/', UserRolDetail.as_view(), name='account_role_detail'),
    path('roles/<int:id>/editar/', UserRolUpdate.as_view(), name='account_role_update'),
    path('roles/<int:id>/eliminar/', UserRolDelete.as_view(), name='account_role_delete'),
    path('roles/<int:id>/asignar/', UserRolAssign.as_view(), name='account_role_assign'),
    path('roles/<int:id>/quitar/', UserRolRemove.as_view(), name='account_role_remove'),
]

