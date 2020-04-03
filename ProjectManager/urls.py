from django.contrib import admin
from django.urls import path, include

from loginAuth import urls as loginauth_urls
from account import urls as account_urls
from proyecto import urls as proyecto_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(account_urls)),
    path('', include(loginauth_urls)),
    path('proyecto/', include(proyecto_urls)),
]
