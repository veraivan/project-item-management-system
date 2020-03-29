from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'required': True,
        'placeholder': 'Escriba su nombre',
        'id': 'nombre',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 
        'required': True,
        'placeholder': 'Escriba su email',
        'id': 'email',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 
        'required': True,
        'placeholder': 'Escriba su contraseña',
        'id': 'contraseña',
    }))
    fields = '__all__'
