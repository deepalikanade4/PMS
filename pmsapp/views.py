from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from .forms import Userloginform,UserRegistrationform
from django.contrib import messages
# from .models import usermodel
# Create your views here.

def signuppage(request):
    if request.method=='POST':
        form=UserRegistrationform(request.POST)
        
        if form.is_valid():
            form.save()
            # usermodel.save(self=usermodel,update_fields=['username','password'])
            message=messages.success(request,"registred successfully")
           




        return redirect(loginpage)
    
    else:
        form=UserRegistrationform()
        return render(request,'pmsapp/signup.html',{'form':form})



def loginpage(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
    #         message=""
            form=Userloginform(request=request,data=request.POST)
            if form.is_valid():
    #             # form.save()
                user=authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])

                if user is not None:
                    login(request,user)
                    message=messages.success(request,message="Login successfully")
                    return render(request,'pmsapp/loginpage.html')
            else:
                # message=messages.success(request,message="login Not success")  
                msg='form not valid'
                return render(request,'pmsapp/loginpage.html',{'form':form})


            
            # return HttpResponseRedirect('/detailpage/')
    #         # msg="login Successfully{}".format(uname)
                

        else:
            form=Userloginform()
            # msg='get method'
            return render(request,'pmsapp/loginpage.html',{'form':form})
    else:
        form=Userloginform()
        msg="you are athenticated"
        return render(request,'pmsapp/loginpage.html',{'form':form,'msg':msg})
