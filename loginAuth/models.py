"""
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()
"""