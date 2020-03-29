from django.shortcuts import render
from django.views.generic import View
from .forms import UsuarioForm
from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0
# Create your views here.


class Registro(View):
    def get(self, request):
        form = UsuarioForm()
        return render(request, 'account/registroUsuario.html', {'form': form})

    def post(self, request):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            guardarUsuarioSSO(form.cleaned_data)
            form.save()
            valor = True
        return render(request, 'index.html', {'mensaje_valido': valor})


def guardarUsuarioSSO(usuario):
    dominio = 'authentication-django.auth0.com'
    client_id = '3sWyFJccKrRs3wH52bgQJFX9im4wS0Qp'
    client_secret = 'my82yHs9ZSmb-frFvlLWAEUhVGZwAuyaxlfOR6Ggi1gvWf1FqVQO0Lzfm-uQfPTE'

    # Nos autenticamos al sso y no responde con un token
    get_token = GetToken(dominio)
    token = get_token.client_credentials(client_id, client_secret, 'https://{}/api/v2/'.format(dominio))
    api_token = token['access_token']

    # Enviar token
    auth0 = Auth0(dominio, api_token)

    # Enviamos el nuevo usuario al SS0
    auth0.users.create({
        'connection': 'Username-Password-Authentication',
        'email': usuario['email'],
        'password': usuario['password'],
        'nickname': usuario['username']
    })