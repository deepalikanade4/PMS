from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login 
# from django.contrib.auth.models import User
from .forms import Userloginform,UserRegistrationform
from django.contrib import messages
from .models import UserModel
from django.views.decorators.csrf import requires_csrf_token

# Create your views here.

def signuppage(request):
    if request.method=='POST':
        form=UserRegistrationform(request.POST)
        if form.is_valid():
            form.save()
            message=messages.success(request,"registred successfully")
           
        return redirect(loginpage)
    
    else:
        form=UserRegistrationform()
        return render(request,'pmsapp/signup.html',{'form':form})


@requires_csrf_token
def loginpage(request):
    # if not request.user.is_authenticated:
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
                return render(request,'pmsapp/dashbord.html')
        else:
            # message=messages.success(request,message="login Not success")  
            msg='form not valid'
            return render(request,'pmsapp/login.html',{'form':form})
        
        # return HttpResponseRedirect('/detailpage/')
#         # msg="login Successfully{}".format(uname)
    else:
        form=Userloginform()
        msg='get method'
        return render(request,'pmsapp/login.html',{'form':form,'msg':msg})
    # else:
    #     form=Userloginform()
    #     msg="you are athenticated"
    #     return render(request,'pmsapp/dashbord.html',{'form':form,'msg':msg})
