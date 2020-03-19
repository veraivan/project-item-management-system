from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode


def index(request):
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
        return render(request, 'index.html')


@login_required
def dashboard(request):
    """
    La funcion dasboard es lanzada una vez que el usuario se autentica, mediante el decorador
    login_required y le redireciona al menu principal del sistema.
    """
    user = request.user
    return render(request, 'dashboard.html', {})


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