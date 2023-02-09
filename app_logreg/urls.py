from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register',views.register,name="register"),
    path('home',views.home,name="home"),
    path('',auth_views.LoginView.as_view(template_name='app_logreg/login.html'),name="login"),
]
