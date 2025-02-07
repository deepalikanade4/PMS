from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path("",views.signuppage,name='signup'),
    path("login",views.loginpage,name='login'),
    path("hr_dashboard",views.hr_dashboard,name='hr_dashboard'),

]