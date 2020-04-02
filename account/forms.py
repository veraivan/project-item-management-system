from django import forms

from .models import ProjectUser
from django.contrib.auth.models import Group, Permission


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = ProjectUser
        fields = ['email', 'username', 'password']

class ModificarDatosForm(forms.ModelForm):
    class Meta:
        model=ProjectUser
        fields = ['email', 'username']

class UserRolForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']

