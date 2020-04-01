from django.urls import include, path

from .views import Registro, dashboard, logout, loggin

urlpatterns = [
    path('', loggin, name='account_loggin'),
    path('dashboard/', dashboard, name='account_dashboard'),
    path('logout/', logout, name='account_logout'),
    path('registro/', Registro.as_view(), name='account_registro'),
]

