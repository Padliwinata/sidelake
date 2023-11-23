from django.urls import path, include
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('/login', views.login_page, name='login'),
    path('/logout', views.handle_logout, name='logout')
]
