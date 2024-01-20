# from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserCreationForm,UsernameField,AuthenticationForm
from django import forms
from django.utils.translation import gettext,gettext_lazy as _
from .models import UserModel
# from django.contrib.auth import get_user_model
# User = get_user_model()

class UserRegistrationform(UserCreationForm):
    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # designation=forms.CharField(max_length=100)
    # email=forms.EmailField(max_length=200)
    class Meta:
        model=UserModel
        fields=['username','designation','email']
        widget={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'designation':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            #'password1' : forms.PasswordInput(attrs={'class':'form-control'
        }


class Userloginform(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    class Meta:
        model=UserModel
        fields=['username','password']
