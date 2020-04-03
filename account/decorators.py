from django.conf import settings
from django.contrib.auth import get_user
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import View


def require_authenticated_permission(permission):

    def decorator(cls):
        if not isinstance(cls, type) or not issubclass(cls, View):
            raise ImproperlyConfigured("required_authenticated_permission must be applied to subclasses of View class.")
        check_auth = method_decorator(login_required)
        check_perm = method_decorator(permission_required(permission, raise_exception=True))
        cls.dispatch = check_auth(check_perm(cls.dispatch))
        return cls

    return decorator

