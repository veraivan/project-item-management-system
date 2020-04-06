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
			'gerente',
		]
		#Etiquetas

		labels = {
			'nombre':'Nombre',
			'gerente':'Gerente',	
		}

		widgets = {
			'nombre': forms.TextInput(),
			'gerente':forms.Select(),
		}