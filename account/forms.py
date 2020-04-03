from django import forms

from .models import ProjectUser


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = ProjectUser
        fields = ['email', 'username', 'password']