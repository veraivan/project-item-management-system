from django.contrib.auth.models import Permission, Group
from account.models import ProjectUser
from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0

aut_group = Group.objects.create(name='Autorizado')
aut_group.permissions.add(Permission.objects.get(codename='see_page'))

admin = ProjectUser.objects.create_user("admin@admin.com", "admin", "admin")
admin_group = Group.objects.create(name='Administrador')
for permission in Permission.objects.all():
    admin_group.permissions.add(permission)
admin.groups.add(admin_group)


