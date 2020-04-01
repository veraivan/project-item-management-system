from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode

from django.urls import reverse_lazy
from django.views.generic import View
from .forms import UsuarioForm, UserRolForm
from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0
from django.contrib.auth.models import Group
from .models import ProjectUser
from .decorators import require_authenticated_permission

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
        'nickname': usuario['username'],
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
#@permission_required('account.see_page', raise_exception=True)
def dashboard(request):
    """
    La funcion dasboard es lanzada una vez que el usuario se autentica, mediante el decorador
    login_required y le redireciona al menu principal del sistema.
    """
    user = request.user
    return render(request, 'account/dashboard.html', {})

@login_required
#@permission_required('account.see_page', raise_exception=True)
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


@require_authenticated_permission('account.see_page')
class UserRolList(View):

    def get(self, request):
        return render(request, 'roles/list.html', {'roles': Group.objects.all()})


@require_authenticated_permission('account.see_page')
class UserRolCreate(View):
    template_name = 'roles/create.html'
    form_class = UserRolForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect('/roles/')
            #return redirect(new_object)
        else:
            return render(request, self.template_name, {'form': bound_form})


@require_authenticated_permission('account.see_page')
class UserRolDetail(View):
    template_name = 'roles/detail.html'

    def get(self, request, id):
        rol = get_object_or_404(Group, id=id)
        return render(
            request,
            self.template_name,
            {'rol': rol})


@require_authenticated_permission('account.see_page')
class UserRolUpdate(View):
    template_name = 'roles/edit.html'
    form_class = UserRolForm
    model = Group

    def get(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        context = {'form': self.form_class(instance=obj),
                   self.model.__name__.lower(): obj}
        return render(request, self.template_name, context)

    def post(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        bound_form = self.form_class(request.POST, instance=obj)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect('/roles/{}'.format(id))
        else:
            context = {'form': bound_form,
                       self.model.__name__.lower(): obj}
            return render(request, self.template_name, context)


@require_authenticated_permission('account.see_page')
class UserRolAssign(View):
    model = Group
    template_name = 'roles/assign.html'

    def get(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        context = {'users': ProjectUser.objects.all(),
                   self.model.__name__.lower(): obj}
        return render(request, self.template_name, context)

    def post(self, request, id):
        users = request.POST.getlist('asignar')
        role = get_object_or_404(Group, id=id)
        for user in users:
            user1 = get_object_or_404(ProjectUser, username=user)
            user1.groups.add(role)
        return redirect('/roles/{}'.format(id))


@require_authenticated_permission('account.see_page')
class UserRolDelete(View):
    model = Group
    success_url = reverse_lazy('account_role_list')
    template_name = 'roles/delete.html'

    def get(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        context = {self.model.__name__.lower(): obj}
        return render(request, self.template_name, context)

    def post(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        obj.delete()
        return HttpResponseRedirect(self.success_url)


