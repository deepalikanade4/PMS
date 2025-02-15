# from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserCreationForm,UsernameField,AuthenticationForm
from django import forms
from django.utils.translation import gettext,gettext_lazy as _
from .models import Login,Kra

class UserRegistrationform(UserCreationForm):
    class Meta:
        model=Login
        
        fields=['username','password','designation','department','emp_code']
        widget={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'designation':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
        }
        def save(self, commit=True):
                
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password"])  # Hash the password
            if commit:
                user.save()

            return user

class Userloginform(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'})
    )
    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
    
    role_choiches=[('HR','HR'),
                   ('Reviewer','Reviewer'),
                   ('Employee','Employee')]
    role=forms.ChoiceField(choices=role_choiches,label='Role',required=False)

class HRDashboardForm(forms.Form):
    department = forms.ModelChoiceField(
        queryset=Login.objects.values_list('department', flat=True).distinct(),
        required=False,
        label="Department "
    )
    designation = forms.ModelChoiceField(
        queryset=Login.objects.values_list('designation', flat=True).distinct(),
        required=False,
        label="Designation ")
    
    primary_reviewer = forms.ModelChoiceField(
        queryset=Login.objects.values_list('username',flat=True).distinct(),
        required=False, 
        label="primary reviewer ")
    
    secondary_reviewer=forms.ModelChoiceField(
        queryset=Login.objects.values_list('username',flat=True).distinct(),
        required=False, 
        label="secondary reviewer ")
    

    year = forms.DateField(required=False, label="Year ")

# class GenerateKraForm(forms.Form):
#     Add_Question=forms.Textarea()
#     answer_choice=[('Textarea'),'YES/NO_Radio','1-5_RatingRadio']
    


class KRAResponseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kra_instances = kwargs.pop('Kra', None)  # Get KRA instances
        super(KRAResponseForm, self).__init__(*args, **kwargs)

        if kra_instances:
            for kra in kra_instances:
                field_name = f"kra_{kra.kra_id}"  # Dynamic field name
                
                if kra.ans_type == 'rating':
                    self.fields[field_name] = forms.ChoiceField(
                        choices=[(str(i), str(i)) for i in range(1, 6)],  # Rating 1-5
                        widget=forms.RadioSelect,
                        label=kra.kra_questions
                    )
                
                # elif kra.ans_type == 'radio':
                #     self.fields[field_name] = forms.ChoiceField(
                #         choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3')],  
                #         widget=forms.RadioSelect,
                #         label=kra.kra_questions
                #     )





                elif kra.answer_type == 'yesno':
                    self.fields[field_name] = forms.ChoiceField(
                        choices=[('yes', 'Yes'), ('no', 'No')],
                        widget=forms.RadioSelect,
                        label=kra.kra_questions
                    )

