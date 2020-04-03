from django.urls import path

from . import views

urlpatterns = [
    path('delete/<int:pk>', views.HistoryDelete.as_view(), name='history_delete'),
    path('', views.ListaHistorial.as_view(), name='history'),
]