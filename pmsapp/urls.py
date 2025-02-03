from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path("",views.signuppage,name='signup'),
    path("login",views.loginpage,name='login')

]