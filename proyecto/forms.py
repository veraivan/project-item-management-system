from django import forms
from proyecto.models import Proyecto

class ProyectoForm(forms.ModelForm):
	"""
	Formulario para poder manipular los datos para la creacion de proyectos
	"""
	class Meta:
		model = Proyecto

		fields = [
			'nombre',
			'estado',
			'fecha_creacion',
			'gerente',
		]
		#Etiquetas

		labels = {
			'nombre':'Nombre',
			'estado':'Estado',
			'fecha_creacion':'Fecha de creacion',
			'gerente':'Gerente',	
		}

		OPCIONES = [('Pendiente','Pendiente'),('Cancelado','Cancelado'),('Iniciado','Iniciado'),('Finalizado','Finalizado')]


		widgets = {
			'nombre': forms.TextInput(),
			'estado':forms.Select(choices=OPCIONES),
			'fecha_creacion':forms.DateInput(),
			'gerente':forms.Select(),
		}