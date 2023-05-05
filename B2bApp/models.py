from django.db import models
from autoslug import AutoSlugField
from django.utils.safestring import mark_safe
from base.models import BaseModel
from django.utils import timezone
from AccountApp.city import STATE_CHOICES,cities
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField

# Create your models here.



class Category(models.Model):
    company=models.ManyToManyField('CompanyInfo')
    color=ColorField(default='#FF0000')
    icon=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    slug=AutoSlugField(populate_from='name',unique=True, null=True, default=None)
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    company=models.ManyToManyField('CompanyInfo')
    name=models.CharField(max_length=100)
    slug=AutoSlugField(populate_from='name',unique=True, null=True, default=None)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['name']
    
class CompanyInfo(models.Model):
    Company_name=models.CharField(max_length=50)
    Company_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Company_subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    Company_slug = AutoSlugField(populate_from='Company_category',unique=True, null=True, default=None)
    Company_color1=ColorField(default='#f8f9fa')
    Company_color2=ColorField(default='##dc3545')
    Company_location=models.CharField(choices=cities,max_length=50)
    Company_brochure=models.FileField(upload_to="Company_pdf",null=True,blank=True)
    Company_description=RichTextField()
    Company_logo=models.ImageField(upload_to="companylogo",null=True,blank=True)
    Company_banner=models.ImageField(upload_to="Companybanner",null=True,blank=True)
    Company_subbanner=models.ImageField(upload_to="Companysubbanner",null=True,blank=True)
    Company_year_of_Establishment=models.CharField(max_length=50)
    Company_about=RichTextField()
    Company_nature_of_business=models.CharField(max_length=100,null=True,blank=True)
    Company_ceo=models.CharField(max_length=100,null=True,blank=True)
    Company_corporate_address=models.CharField(max_length=100,null=True,blank=True)
    Company_registed_address=models.CharField(max_length=100,null=True,blank=True)
    Company_industry=models.CharField(max_length=100,null=True,blank=True)
    Company_total_employee=models.CharField(max_length=100,null=True,blank=True)
    Company_legal_status_of_firm=models.CharField(max_length=100,null=True,blank=True)
    Company_pan_no=models.CharField(max_length=100,null=True,blank=True)
    Company_gts_no=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.Company_name 
    
    class Meta:
        ordering=['Company_name']
    
    def delete(self,*args, **kwargs):
        self.Company_logo.delete()
        return super(CompanyInfo, self).delete(*args, **kwargs)

    # def admin_photo(self):
    #     return mark_safe('<img src="{}" width="100" />'.format(self.Company_logo.url))
    # admin_photo.short_description ='Company_logo'
    # admin_photo.allow_tag =True

class Company_Additional_Business(models.Model):
    company=models.ForeignKey(CompanyInfo,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True,blank=True)

class  Franchise_company_banner(models.Model):
     company=models.ForeignKey(CompanyInfo,on_delete=models.CASCADE)
     banner= models.ImageField(upload_to="Companysubbanner/franchies/banner",null=True,blank=True)
    
class Product(models.Model):
    company=models.ManyToManyField('CompanyInfo')
    Product_name=models.CharField(max_length=100)
    Product_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    Product_slug = AutoSlugField(populate_from='Product_name',unique=True, null=True, default=None)
    Product_image=models.ImageField(upload_to="Productimg")
     
    def __str__(self):
        return self.Product_name
    
    class Meta:
        ordering=['Product_name']
    
    def delete(self,*args, **kwargs):
        self.Product_image.delete()
        return super(Product, self).delete(*args, **kwargs)

    def product_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Product_image.url))
    product_image.short_description ='Product_image'
    product_image.allow_tag =True


class SendPage(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=14)
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=254)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
