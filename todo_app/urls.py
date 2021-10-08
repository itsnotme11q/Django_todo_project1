from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',login_page,name="login_page"),
    path('home',home,name="home"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('todo',todo,name="todo"),
    path('todo_delete/<id>',todo_delete,name="todo_delete"),
    path('is_complete_fun/<id>',is_complete_fun,name="is_complete_fun"),
    path('login',login_page,name="login_page"),
    path('logout',logout_page,name="logout_page"),
    path('registration',registration_page,name="registration_page"),
    path('<id>',dynamic_home,name="dynamic_home"),
]
