from django.contrib import admin
from django.urls import path, include

from loginAuth import urls as loginauth_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(loginauth_urls)),
]
