from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('welcome/', views.welcome),
    path('user/', views.check_user),
    path('auth_user/', views.auth_user),



    
]

