from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .forms import Userloginform,UserRegistrationform , HRDashboardForm
from .models import User,Login,Kra
from django.contrib import messages
from django.middleware.csrf import get_token


def signuppage(request):
    csrf_token = get_token(request)
    print("CSRF Token:", csrf_token)
    if request.method=='POST':
        form=UserRegistrationform(request.POST)
        
        if form.is_valid():
            form.save()
            message=messages.success(request,"registred successfully")
        return redirect(loginpage)
    else:
        form=UserRegistrationform()
        return render(request,'pmsapp/signup.html',{'form':form})

def loginpage(request):
    if request.method=='POST':
        form=Userloginform(request,data=request.POST)
        if form.is_valid():
            print('*********************************************')
            user=authenticate(username=form.cleaned_data['username'],
                         password=form.cleaned_data['password'])
            print(user)
            if user is not None:
                print("_________________________________________________")
                login(request,user)
                print(form.cleaned_data['role'])
                if form.cleaned_data['role']=="HR":
                    form=HRDashboardForm()
                    return render(request,'pmsapp/HR_dashboard.html',{'form':form})
                if form.cleaned_data['role']=="Reviewer":
                    return render(request,'pmsapp/dashbord.html',{'form':form})
                if form.cleaned_data['role']=="Employee":
                    return render(request,'pmsapp/dashbord.html',{'form':form})
                
        return render(request,'pmsapp/login.html',{'form':form})

    else:
        form=Userloginform()
    return render(request,'pmsapp/login.html',{'form':form})

#             
#             if user is not None:
#                 login(request,user)
#                 message=messages.success(request,message="Login successfully")

#             return render(request,'pmsapp/dashbord.html')
#         else:
#             # message=messages.success(request,message="login Not success")  
#             msg='form not valid'
#             return render(request,'pmsapp/loginpage.html',{'form':form})


        
        # return HttpResponseRedirect('/detailpage/')
#         # msg="login Successfully{}".format(uname)
            

    # else:
    #     form=Userloginform()
    #     # msg='get method'
        # return render(request,'pmsapp/loginpage.html',{'form':form})
    # else:
    #     form=Userloginform()
    #     msg="you are athenticated"
    #     print("alredy auth  post-------------------------------------")

    #     return render(request,'pmsapp/loginpage.html',{'form':form,'msg':msg})



def hr_dashboard(request):
    form = HRDashboardForm()
    # kra_reports = Kra.objects.select_related('User').all()

    return render(request,'pmsapp\HR_dashboard.html', {
        'form': form,
        # 'kra_reports': kra_reports
    })
