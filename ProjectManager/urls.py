from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from loginAuth import urls as loginauth_urls
from account import urls as account_urls
from proyecto import urls as proyecto_urls
from historial import urls as historial_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(account_urls)),
    path('', include(loginauth_urls)),
    path('proyecto/', include(proyecto_urls)),
    path('history/', include(historial_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

