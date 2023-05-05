from django.shortcuts import render ,redirect
from B2bApp .models import *
from django.views import View
from B2bApp .forms import *
from CommonApp .models import *
from  AccountApp .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from B2bApp  .forms import ContactForm,send_mail
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.template.loader import get_template

# Create your views here.
# below import is done for sending emails

from django.conf import settings
from django.core.mail import message
from django.core.mail import send_mail,EmailMultiAlternatives
from django.core import mail
from django.core.mail.message import EmailMessage
##########################################
######### Home Function Start ############
##########################################   
class HomeView(View):
    def get(self, request):
     category=Category.objects.all()
     company=CompanyInfo.objects.all()
     locations=CompanyInfo.objects.all()
     product=Product.objects.all()
     unq_list=[]
     for i in locations:
       unq_list.append(i.Company_location)
     context={
       "category":Category.objects.all(),
       "location":set(unq_list),
        'product':product,
        "company":company,
        "logo":WebsiteLogo.objects.all(),
        "form":SubscriberForm(),
        "category":category
     }
     return render(request, 'b2b/index.html',context)
##########################################
######### Home Function End ##############
##########################################  

##########################################
######### About Function Start ###########
##########################################  
class AboutView(View):
    def get(self, request):
     context={
        "logo":WebsiteLogo.objects.all()
     }
     return render(request, 'b2b/about.html',context)
##########################################
######### About Function end #############
########################################## 
 
##########################################
######### Contact Function start #########
##########################################
class ContactView(FormView):
    template_name = 'b2b/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('B2bApp:success')
    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)
    def get(self,request):
      context={
         "logo":WebsiteLogo.objects.all(),
          "form":ContactForm
      }
      return render(request,self.template_name,context)
##########################################
######### Contact Function End ###########
##########################################   
class ContactSuccessView(TemplateView):
    
    template_name = 'b2b/success.html'

##########################################
############# Category Function ##########
##########################################
class CategoryView(View):
    def get(self, request):
     product=Product.objects.all()
     
     context={
       'product':product,
        "logo":WebsiteLogo.objects.all()
     }
     return render(request, 'b2b/category.html',context)
##########################################
############# Category Function ##########
##########################################

##########################################
############# Listing Function ###########
##########################################
class ListingView(View):
 def get(self,request):
    products=CompanyInfo.objects.all()
    subCategorys=SubCategory.objects.all()
    all_page=CompanyInfo.objects.all()
    paginator=Paginator(all_page,7)
    page_no=request.GET.get('page')
    page_obj=paginator.get_page(page_no)
    locations=CompanyInfo.objects.all()
    unq_list=[]
    for i in locations:
       unq_list.append(i.Company_location)
       context={
         'products':products,
         'subCategorys':subCategorys,
         'page_obj':page_obj,
         "category":Category.objects.all(),
         "location":set(unq_list),
          "logo":WebsiteLogo.objects.all()
         }
    return render(request, 'b2b/listings.html',context)
##########################################
############# Listing Function ###########
##########################################

##########################################
######### Fliter cate Function start #####
##########################################
class FilterCategory(View):
  def get(self,request):
     cate_name_get=request.GET.get('cate')
     get_filter_id=Category.objects.filter(name=cate_name_get)[0]
     filterdata=CompanyInfo.objects.filter(Company_location=request.GET.get('loc'),Company_category=get_filter_id.id)
     subCategorys=SubCategory.objects.all()
     all_page=filterdata
     paginator=Paginator(all_page,7)
     page_no=request.GET.get('page')
     page_obj=paginator.get_page(page_no)
     data_filtered=[]
     for i in filterdata:
      if str(i.Company_category)==request.GET.get('cate'):
       data_filtered.append(i)
     locations=CompanyInfo.objects.all()
     unq_list=[]
     for i in locations:
      unq_list.append(i.Company_location)
     context={
      "page_obj":data_filtered,
       "category":Category.objects.all(),
      'subCategorys':subCategorys,
       "location":set(unq_list),
       "page_obj":page_obj,
        "logo":WebsiteLogo.objects.all()
     }
     return  render(request, 'b2b/listings.html',context)
  
##########################################
######### Fliter cate Function end #######
##########################################

##########################################
######### Fliter cate Function start #####
##########################################  
class FilterCate(View):
  def get(self,request,id):
     data=Category.objects.get(pk=id)
     filterdata=data.company.all()
     subCategorys=SubCategory.objects.all()
     all_page=filterdata
     paginator=Paginator(all_page,7)
     page_no=request.GET.get('page')
     page_obj=paginator.get_page(page_no)
     data_filtered=[]
     for i in filterdata:
      if str(i.Company_category)==request.GET.get('cate'):
       data_filtered.append(i)
     locations=CompanyInfo.objects.all()
     unq_list=[]
     for i in locations:
      unq_list.append(i.Company_location)
     context={
      "page_obj":data_filtered,
       "category":Category.objects.all(),
      'subCategorys':subCategorys,
       "location":set(unq_list),
       "page_obj":page_obj,
        "logo":WebsiteLogo.objects.all()
     }
     return  render(request, 'b2b/listings.html',context)
##########################################
######### Fliter cate Function end #######
##########################################    

##########################################
######### Fliter loc Function start ######
##########################################  
class Filterlocation(View):
    def get(self,request,loc):
     filterdata=CompanyInfo.objects.filter(Company_location=loc)
     locations=CompanyInfo.objects.all()
     subCategorys=SubCategory.objects.all()
     all_page=filterdata
     paginator=Paginator(all_page,7)
     page_no=request.GET.get('page')
     page_obj=paginator.get_page(page_no)
     unq_list=[]
     for i in locations:
       unq_list.append(i.Company_location)
          
     context={
        "page_obj":filterdata,
       "location":set(unq_list),
       'subCategorys':subCategorys,
        "page_obj":page_obj,
         "logo":WebsiteLogo.objects.all()

          }
     return  render(request, 'b2b/listings.html',context)
##########################################
######### Fliter loc Function end ########
##########################################  

##########################################
###### Fliter Subcate Function start #####
##########################################  
class FilterSubcategory(View):
    def get(self,request,id):
     data=Product.objects.get(pk=id)
     filterdata=data.company.all()
     locations=CompanyInfo.objects.all()
     subCategorys=SubCategory.objects.all()
     all_page=filterdata
     paginator=Paginator(all_page,7)
     page_no=request.GET.get('page')
     page_obj=paginator.get_page(page_no)
     unq_list=[]
     for i in locations:
       unq_list.append(i.Company_location)
          
     context={
        "page_obj":filterdata,
       "location":set(unq_list),
       'subCategorys':subCategorys,
        "page_obj":page_obj,
         "logo":WebsiteLogo.objects.all()
        }
     return  render(request, 'b2b/listings.html',context)
##########################################
######## Fliter Subcate Function end #####
##########################################    

##########################################
########## SendFunction start ###########
##########################################  
class SendQuery(View):
  def post(self,request):
   if request.method == 'POST':
     name=request.POST.get('name')
     email=request.POST.get('emailid')
     phone=request.POST.get('number')
     message=request.POST.get('mes')
     obj_query=SendPage.objects.create(name=name,email=email,phone=phone,message=message)
     obj_query.save()
     #emails sending starts from here
     from_email=settings.EMAIL_HOST_USER
     connection=mail.get_connection()
     connection.open()
     email_message=mail.EmailMessage(f'{email}',f'Name: {name}\nEmail : {email}\nPhone: {phone}\nQUERY : {message}',from_email,['pharmastar64@gmail.com','pharmastar64@gmail.com'],connection=connection)
     #   email_client=mail.EmailMessage('PharmaXpert Response','Thanks For Reaching us\n\nPharmaXpert.com\n\nofficialmitsmarketing@gmail.com',connection=connection)
     #   connection.send_messages([email_message,email_client])
     connection.send_messages([email_message])
     connection.close()
     #   messages.info(request,"Thanks For Reaching Us! We will get back you soon....")
     context={
        "logo":WebsiteLogo.objects.all()
     }
     return redirect('B2bApp:success',context)
   context={
      "logo":WebsiteLogo.objects.all()
   }
   return render (request,'b2b/success.html',context)
##########################################
############ send Function end ###########
##########################################  

##########################################
######### Serach Function start ##########
##########################################  
class Serach(View):
  def get(self,request):
     search=request.GET.get('look')
     filterdata=CompanyInfo.objects.filter(Q(Company_name__icontains=search) | Q(Company_category__name__icontains=search) | Q( Company_subcategory__name__icontains=search) | Q(Company_location__icontains=search))
    #  if filterdata.exists():
    #     filterdata=CompanyInfo.objects.filter(Q(Company_name__icontains=search) | Q(Company_category__name__icontains=search) | Q( Company_subcategory__name__icontains=search))
    #  else:
    #    return redirect ('404')
     subCategorys=SubCategory.objects.all()
     all_page=filterdata
     paginator=Paginator(all_page,7)
     page_no=request.GET.get('page')
     page_obj=paginator.get_page(page_no)
     data_filtered=[]
     for i in filterdata:
      if str(i.Company_category)==request.GET.get('cate'):
       data_filtered.append(i)
     locations=CompanyInfo.objects.all()
     unq_list=[]
     for i in locations:
      unq_list.append(i.Company_location)
     context={
      "page_obj":data_filtered,
       "category":Category.objects.all(),
      'subCategorys':subCategorys,
       "location":set(unq_list),
       "page_obj":page_obj,
        "logo":WebsiteLogo.objects.all()
     }
     return  render(request, 'b2b/listings.html',context)

##########################################
######### Serach Function end ############
##########################################  

def subscribe(request):
    if request.method == 'POST':
        form =SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save(commit=False)
            subscriber.save()
            subscribers = Subscriber.objects.all()
            subject = 'Welcome to PharmaXpert'
            message = 'Thank you for subscribing to our newsletter'
            from_email =settings.EMAIL_HOST_USER
            recipient_list = [subscriber.email or subscriber.name for subscriber in subscribers]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('B2bApp:success')
    else:
        form = SubscriberForm()
    return render(request, 'b2b/index.html', {'form': form})