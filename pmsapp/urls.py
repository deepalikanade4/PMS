from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path("",views.signuppage,name='signup'),
    path("login",views.loginpage,name='login'),
    path("hr_dashboard",views.hr_dashboard,name='hr_dashboard'),
    path('generatekra',views.generatekra,name='generate_kra'),
    path('self_assmt_form/<str:emp_code>/',views.generate_kra_form,name='generate_kra_form'),

]