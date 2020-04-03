from django.urls import include, path

from loginAuth import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]

