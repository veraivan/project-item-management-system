from django.urls import include, path

from loginAuth import views

urlpatterns = [
    path('', views.index),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout),
]

