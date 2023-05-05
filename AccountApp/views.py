from django.shortcuts import render
from django.views import View
from CommonApp .models import *
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from  AccountApp .models import *
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
from .forms import *
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy


#password change package
from django.db.models.query_utils import Q
from .models import Profile
from  AccountApp .helper import send_forget_password_mail
# below import is done for sending emails
from django.conf import settings
from django.core.mail import message
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage
# Create your views here.
##########################################
############# login Function #############
##########################################
def login_page(request):
      if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(email = email)
        if user_obj.count()>0:
            if user_obj[0].is_superuser == True:
                user_obj_l = authenticate(username = user_obj[0].username , password= password)
                if user_obj_l:
                    login(request , user_obj[0])
                    return redirect('/admin/')
            else:
                if not user_obj.exists():
                    messages.warning(request, 'Account not found.')
                    return HttpResponseRedirect(request.path_info)
                if not user_obj[0].profile.is_email_verified:
                    messages.warning(request, 'Your account is not verified.')
                    return HttpResponseRedirect(request.path_info)
                user_obj = authenticate(username = email , password= password)
                if user_obj:
                    login(request , user_obj)
                    return redirect('/')
        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)
      context={
            "logo":WebsiteLogo.objects.all()
      }
      return render(request, 'account/login.html',context)
##########################################
############# login Function #############
##########################################
    
##########################################
############# Signup Function ############
##########################################
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)      
        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)
        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)
    context={
            "logo":WebsiteLogo.objects.all()
      }
    return render(request ,'account/signup.html',context)
##########################################
############# Signup Function ############
##########################################


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/account/login/')
        # return render(request, 'account/login.html')
##########################################
######### Token Veriyfy Function #########
##########################################
def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')
##########################################
######### change Password Function #######
##########################################
import uuid
def changepassword(request , token,id):
    context = {}
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            # id= str(uuid.uuid4())
            user_id = id
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'AccountApp:change-password/{token}/{id}')
      
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'AccountApp:change-password/{token}/{id}')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()

            return redirect('/account/login/')
            
            
    except Exception as e:
        context={
            "logo":WebsiteLogo.objects.all()
      }
        print(e)
    return render(request , 'account/changepassword.html' , context)


##########################################
######### change Password Function #######
########################################## 

##########################################
######### forget Password Function #######
##########################################
import uuid
def forgetpassword(request):
    try: 
       if request.method =='POST':
           email=request.POST.get('email')

           if not User.objects.filter(email=email).first():
               messages.success(request,'Not user found with this email.')
               return redirect ('AccountApp:forget_password')
           
       user_obj = User.objects.get(email = email)
       token = str(uuid.uuid4())
       id=user_obj.id
       profile_obj=Profile.objects.get(user =user_obj)
       profile_obj.forget_password_token =token
       profile_obj.save()
       send_forget_password_mail(user_obj, token,id)
       messages.success(request,'An Email is Sent')
       return redirect ('AccountApp:forget_password')
           
    except Exception as e:
        context={
            "logo":WebsiteLogo.objects.all()
      }
        print(e)
    return render(request,'account/forgetpassword.html',context)
##########################################
######### forget Password Function #######
##########################################

class PosttView(View):
  def get(self,request):
      state=PostRequirement.objects.filter(PostRequirement=state)
      print(state)
      return render(request,'b2b/success.html',{'state':state})
  def post(self,request):
    
    if request.method=='POST':
      email=request.POST.get('email')
      category=request.POST.get('category')
      duretion=request.POST.get('duretion')
      state=request.POST.get('state')
      city=request.POST.get('city')
      time=request.POST.get('time')
      phone=request.POST.get('phone')
      message=request.POST.get('mess')
      query=PostRequirement.objects.create( email=email ,category=category, duretion=duretion, time=time,state=state,city=city, phone=phone, message=message)
      query.save()
      # emails sending starts from here
      from_email=settings.EMAIL_HOST_USER
      connection=mail.get_connection()
      connection.open()

      email_message=mail.EmailMessage(f'{email}',f'Category: {category}\nDuretion : {duretion}\nTime: {time}\nState : {state}\nCity : {city}\nNumber : {phone}\nQUERY : {message}',from_email,['pharmastar64@gmail.com','pharmastar64@gmail.com'],connection=connection)
    #   email_client=mail.EmailMessage('PharmaXpert Response','Thanks For Reaching us\n\nPharmaXpert.com\n\nofficialmitsmarketing@gmail.com',connection=connection)
    #   connection.send_messages([email_message,email_client])
      connection.send_messages([email_message])
      connection.close()
    #   messages.info(request,"Thanks For Reaching Us! We will get back you soon....")
   
      return redirect('AccountApp:success_pro')

    return render(request,'b2b/success.html')

class ContactSuccessView(TemplateView):
    template_name = 'account/success.html'
