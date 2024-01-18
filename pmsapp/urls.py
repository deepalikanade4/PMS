from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.signuppage,name="signup"),
    path("login",views.loginpage,name='login'),
]