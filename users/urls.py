from re import template
from django.urls import path
from django.contrib.auth import views as user_auth
from . import views as users_view

urlpatterns=[
    path('login/',user_auth.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',user_auth.LogoutView.as_view(template_name='users/main.html'),name='logout'),
    path('register/',users_view.register,name='register'),
    path('profile/',users_view.profile,name='profile'),
    path('main/',users_view.main,name='main'),
]