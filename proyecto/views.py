from django.shortcuts import render
from django.views.generic import (
	ListView, 
	CreateView, 
	UpdateView
)
from proyecto.models import Proyecto
from proyecto.forms import ProyectoForm
from django.urls import reverse_lazy


class ProyectoView(ListView):
	"""
	Vista basada en clase el cual lista todos los proyectos
	"""
	model = Proyecto
	template_name = 'proyecto/proyecto_list.html'

class ProyectoCreate(CreateView):
	"""
	Vista basada en clase el sirve para crear un proyecto nuevo
	"""
	model = Proyecto  #Indicar el modelo a utilizar
	form_class = ProyectoForm #Indicar el formulario
	template_name = 'proyecto/proyecto_form.html' #Indicar el template
	success_url = reverse_lazy('proyecto_listar') #Redireccionar 

class ProyectoUpdate(UpdateView):
	"""
	Vista basada en clase el sirve para crear un proyecto nuevo
	"""
	model = Proyecto #Indicar el modelo a utilizar
	form_class = ProyectoForm #Indicar el formulario
	template_name = 'proyecto/proyecto_form.html' #Indicar el template
	success_url = reverse_lazy('proyecto_listar') #Redireccionar 
