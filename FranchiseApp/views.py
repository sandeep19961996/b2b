from django.shortcuts import render,redirect
from django.views import View
from FranchiseApp .models import *
from CommonApp .models import *
from B2bApp.models import *
import random
from django.db.models import Count
# below import is done for sending emails
from django.conf import settings
from django.core.mail import message
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage
# Create your views here. 
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
import uuid

##########################################
########## mitshealthcare views ##########
##########################################
class HomeView(View):
    def get(self,request,pk):
    #  pk=str(uuid.uuid4())
     comp=CompanyInfo.objects.get(pk = pk)
     product=MitsProducts.objects.filter(company_id=pk)
     company=CompanyInfo.objects.get(pk = pk)
     print(company)
     banner=Franchise_company_banner.objects.filter(company_id=pk)
     business=Company_Additional_Business.objects.filter(company_id=pk)
     context={
        "product":product,
        'company':company,
        "banner":banner,
        'business': business,
        "logo":WebsiteLogo.objects.all(),
        "comp":comp
        }
     return render(request,'mitsheathcare/index.html',context)
    
class AboutView(View):
    def get(self,request,pk):
        comp=CompanyInfo.objects.get(pk = pk)
        company=CompanyInfo.objects.get( pk =pk)
        business=Company_Additional_Business.objects.all()[0:5]
        context={
            'company':company,
            'business': business,
              "logo":WebsiteLogo.objects.all(),
              "comp":comp
        }
        return render(request,'mitsheathcare/about.html',context)

class OurRangeView(View):
    def get(self,request,pk):
        comp=CompanyInfo.objects.get(pk = pk)
        product=MitsProducts.objects.filter(company_id=pk)
        company=CompanyInfo.objects.get(pk=pk)
        context={
        "product":product,
        'company':company,
        "logo":WebsiteLogo.objects.all(),
        "comp":comp
        }
        return render(request,'mitsheathcare/our_range.html',context)

class ContactView(View):
    def get(self,request,pk):
        comp=CompanyInfo.objects.get(pk = pk)
        company=CompanyInfo.objects.get(pk=pk)
        context={
            'company':company,
            "logo":WebsiteLogo.objects.all(),
            "comp":comp
        }
        return render(request,'mitsheathcare/contact.html',context)

class ProductView(View):
    def get(self,request,pk):
         comp=CompanyInfo.objects.get(pk = pk)
         total_issues = MitsProducts.objects.all().filter(company_id=pk).count()
         product=MitsProducts.objects.filter(company_id=pk)
         company=CompanyInfo.objects.get(pk=pk)
        #  comp=MitsProducts.objects.get(pk=pk)
         context={
        "product":product,
         'total_issues': total_issues, 
        #  'comp':comp,
        'company':company,
        "logo":WebsiteLogo.objects.all(),
        "comp":comp
        }
         return render(request,'mitsheathcare/products.html',context)
    
class ProductDetailView(View):
    def get(self,request,pk):
        # comp=CompanyInfo.objects.get(pk=pk)
        detail=MitsProducts.objects.get(pk=pk)
        products = MitsProducts.objects.all().order_by('tags')[:60]
        related = random.sample(list(products) , 4)
        context={
         'detail':detail,
         'related':related,
         'company':detail.company,
         "logo":WebsiteLogo.objects.all(),
          "comp":detail.company
         }
        return render(request,'mitsheathcare/product_detail.html',context)

class SendQuery(View):
  def post(self,request):
   if request.method == 'POST':
     name=request.POST.get('naam')
     email=request.POST.get('mail')
     phone=request.POST.get('no')
     message=request.POST.get('dec')
     query=Send.objects.create( name=name,email=email,phone=phone,message=message)
     query.save()
    #emails sending starts from here
     from_email=settings.EMAIL_HOST_USER
     connection=mail.get_connection()
     connection.open()
     email_message=mail.EmailMessage(f'{email}',f'Name: {name}\nEmail : {email}\nPhone: {phone}\nQUERY : {message}',from_email,['pharmastar64@gmail.com','pharmastar64@gmail.com'],connection=connection)
     #email_client=mail.EmailMessage('PharmaXpert Response','Thanks For Reaching us\n\nPharmaXpert.com\n\nofficialmitsmarketing@gmail.com',connection=connection)
  
     connection.send_messages([email_message])
     connection.close()
     #   messages.info(request,"Thanks For Reaching Us! We will get back you soon....")
     return redirect('B2bApp:success')
   context={
        "logo":WebsiteLogo.objects.all(),
   }
   return render (request,'b2b/success.html',context)
  
