from django.db import models
from account.models import ProjectUser
from django.utils import timezone


class Proyecto(models.Model):
	"""
	Modelo correspondiente a al proyecto

	ATRIBUTOS:
		- nombre: nombre del proyecto.
		- estado: estado actual del proyecto, puede ser:
			-Pendiente: Se podrá realizar modificar los datos del proyecto.
			
			-Cancelado: No se podrán realizar modificación alguna sobre los
				datos del proyecto, ni otras funcionalidades asociadas al mismo.
			
			-Iniciado:Los ítems, líneas bases y relaciones se podrán modificar,
				pero no eliminar dentro de un proyecto
			
			+Finalizado: No se podrá realizar modificación alguna sobre los
				datos del proyecto, pero se podrá visualizar la descripción del mismo.
		- fecha de creacion: contiene la fecha en la que fue creada.
		- gerente: indica quien es el gerente del proyecto
	"""

	nombre = models.CharField(max_length=50)
	estado = models.CharField(max_length=50, default = 'Pendiente')
	fecha_creacion = models.DateTimeField(default=timezone.now)	
	gerente = models.ForeignKey(ProjectUser, null=True, blank = False, on_delete=models.CASCADE)

	def __str__(self):
		"""
		Retorna el nombre del proyecto
		"""
		return self.nombre

	class Meta:
		"""
		Definicion de permisos
		"""
		permissions = (
			('agregar_gerente','Permite agregar un gerente al proyecto'),
			('cambiar_estado','Permite cambiar el estado del proyecto'),
			('modificar_proyecto','Permite modificar los atributos del proyecto sin inicializar'),
			('ver_proyecto', 'Permite al usuario ver los proyectos'),
		)

	


