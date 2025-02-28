from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import Userloginform,UserRegistrationform , HRDashboardForm,KRAResponseForm
from .models import User,Login,Kra,KraId
from django.contrib import messages
from django.middleware.csrf import get_token


import datetime


def signuppage(request):
    csrf_token = get_token(request)
    print("CSRF Token:", csrf_token)
    if request.method=='POST':
        form=UserRegistrationform(request.POST)
        # print("++++++++++++++++++++++++++++++++++++++++++++",form.is_valid())
        if form.is_valid():
            # print("******************************",request.POST.get('username'))
            form.save()
            message=messages.success(request,"registred successfully")
        else:
            print(form.errors)
        return redirect(loginpage)
    else:
        form=UserRegistrationform()
        return render(request,'pmsapp/signup.html',{'form':form})

def loginpage(request):
    if request.method=='POST':
        form=Userloginform(request,data=request.POST)
        if form.is_valid():
            
            user=authenticate(username=form.cleaned_data['username'],
                         password=form.cleaned_data['password'])
            # print(user)
            if user is not None:
                login(request,user)
                # print(form.cleaned_data['role'])
                request.session['empcode'] = user.emp_code 
                if form.cleaned_data['role']=="HR":
                    # user=Login.objects.all
                    return redirect(hr_dashboard)
                    
                if form.cleaned_data['role']=="Reviewer":
                    return render(request,'pmsapp/reviewer_dashboard.html',{'form':form})
                if form.cleaned_data['role']=="Employee":
                    # return render(request,'pmsapp/dashbord.html',{'form':form})
                    # return redirect(generate_kra_form)
                    return redirect(reverse('generate_kra_form', args=[user.emp_code]))
                
        return render(request,'pmsapp/login.html',{'form':form})

    else:
        form=Userloginform()
    return render(request,'pmsapp/login.html',{'form':form})

def hr_dashboard(request):
    if request.method=='POST':
        year=request.POST.get("year")
        department=request.POST.get("department")
        designation=request.POST.get("designation")
        primary_reviewer=request.POST.get("primary_reviewer")
        secondary_reviewer=request.POST.get("secondary_reviewer")
        year_data=KraId.objects.values_list('year','id')
        dept_data=KraId.objects.values_list('department','id')
        design_data=KraId.objects.values_list('designation','id')
  
        if year in [str(year[0])for year in [element for element in year_data]]: 
             matched_dept= [dept for dept in [element for element in dept_data] if department == dept[0]]
            #  print(matched_dept)
             matched_designation=[desig for desig in [element for element in design_data] if designation == desig[0]]
            #  print(matched_designation) 
             if matched_dept and matched_designation:
                 if set([e[1] for e in matched_dept]) & set( [e[1] for e in matched_designation]):
              
                    #  print("matche found",set([e[1] for e in matched_dept]) & set([e[1] for e in matched_designation]))
                     pass
                 else:
                      print('match found but with seperate new entry created ')
                      KraId.objects.create(year=year,department=department,designation=designation)
                     
             else:
                 print("new designation/dept found entry created")
                 KraId.objects.create(year=year,department=department,designation=designation)
        else:
            KraId.objects.create(year=year,department=department,designation=designation)

        current_kra_id=KraId.objects.filter(department=department ,designation=designation,year=year).first()
        
        print(current_kra_id.id)
        return render(request,'pmsapp\generatekraform.html',{'current_kra':int(current_kra_id.id)})

    else:
        form = HRDashboardForm()
        return render(request,'pmsapp\HR_dashboard.html', {'form': form})

def generatekra(request):
   
   if request.method=="POST":
    
    #    print(request.POST.get('action'))
       if request.POST.get('action')=='save_add_new':
           quetion=request.POST.get('question')
           answer_type=request.POST.get('answer_type')
           created_by=request.session.get('empcode', None)
        #    print(created_by)
           created_on=datetime.date.today()
        #    print("****************************************************")
        #    print(request.POST.get('kra_id'))
           try:
                kra_id=KraId.objects.get(id=request.POST.get('kra_id'))
           except KraId.DoesNotExist:
               messages='form is not available'
               return render(request,'pmsapp\login.html',{messages:messages})

           else:
               #    print(kra_id.id)
               Kra.objects.create(kra_id=kra_id,created_by=created_by,added_on=created_on,kra_questions=quetion,answer_type=answer_type)
           return render(request,"pmsapp\generatekraform.html",{'current_kra':kra_id.id})
       elif request.POST.get('action')=='save_submit':

            return render(request,"pmsapp\HR_dashboard.html")
   else:
       return render(request,"pmsapp\generatekraform.html")
   

def generate_kra_form(request,emp_code):
    # print(request,emp_code)
    # if request.method=='POST':
    # print("--------------------------------------------------------------------")
    # print(request.POST.get('emp_code'))
    user=Login.objects.get(emp_code=emp_code)
    # print(user,user.department,user.designation,datetime.datetime.now().year)
    try:
        kra_id=KraId.objects.get(department=user.department,designation=user.designation,year=datetime.datetime.now().year)
    # print(kra_id)
    except:
        messages=['kra form not availbale']
        form=Userloginform()

        return render(request,'pmsapp\login.html',{'messages':messages,'form':form})
    else:
         quetion_Set=Kra.objects.filter(kra_id=kra_id).values_list('kra_questions','answer_type')
    form=KRAResponseForm()
    return render(request,'pmsapp\selfassesmentform.html',{'form':form,'Quetion_answer':list(quetion_Set)})
       
