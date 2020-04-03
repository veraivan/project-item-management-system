from django.urls import path, include
from proyecto.views import ProyectoView, ProyectoCreate, ProyectoUpdate

urlpatterns = [
	path('nuevo/', ProyectoCreate.as_view(), name="proyecto_crear"),
	path('listar/', ProyectoView.as_view(), name="proyecto_listar"),
	path('editar/<int:pk>/', ProyectoUpdate.as_view(), name="proyecto_editar"),
]
