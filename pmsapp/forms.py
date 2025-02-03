# from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserCreationForm,UsernameField,AuthenticationForm
from django import forms
from django.utils.translation import gettext,gettext_lazy as _
from .models import Login

class UserRegistrationform(forms.ModelForm):
    
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # designation=forms.CharField(max_length=100)
    class Meta:
        model=Login
        fields=['username','password','designation']
        widget={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'designation':forms.TextInput(attrs={'class':'form-control'}),
            # 'email':forms.EmailInput(attrs={'class':'form-control'})

        }


class Userloginform(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
