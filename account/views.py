from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
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
        return render(request, 'account/index.html', {'mensaje_valido': valor})


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

def loggin(request):
    """
    La funcion index, se encarga de preguntar si un usuario esta autenticado o no
    Primeramente se declara una variable user y alamacenamos en esa variable el usuario con request,
    y pregunta si el usuario esta autenticado y tambien si es super usuario.
    Ejemplo: si Juan Perez esta logueado y no es super usuario le redireciona al menu principal del sistema,
    caso contrario le lanza la pagina de autentication.
    """
    user = request.user
    if user.is_authenticated and not user.is_superuser:
        return redirect(dashboard)
    else:
        return render(request, 'account/index.html')


@login_required
def dashboard(request):
    """
    La funcion dasboard es lanzada una vez que el usuario se autentica, mediante el decorador
    login_required y le redireciona al menu principal del sistema.
    """
    user = request.user
    return render(request, 'account/dashboard.html', {})


def logout(request):
    """
    La funcion del logout ya se encarga de redireccionar al menu de inicio de sesion
    una vez que el usuario haya presionado el boton de logout.
    Por lo tanto la configuracion hecha hace que HttpResponseRedirect retorne la ruta de inicio
    """
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)

