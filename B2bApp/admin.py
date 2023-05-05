from django.contrib import admin
from B2bApp .models import *
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.


@admin.register(Category)
class CategoryAdmin( admin.ModelAdmin):
    list_display=['name','slug','icon']
  
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']


class Franchise_company_banner(admin.TabularInline):
   model=Franchise_company_banner

class Company_Additional_Business(admin.TabularInline):
   model=Company_Additional_Business

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display=['Company_name','Company_category','Company_subcategory','Company_location','Company_description','Company_slug']
    # readonly_fields = ['admin_photo']
    inlines=[Franchise_company_banner,Company_Additional_Business]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['Product_name','Product_category','Product_slug','product_image']
    readonly_fields=['product_image']


@admin.register(SendPage)
class SendQueryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['name','email','phone','message']


@admin.register(Subscriber)
class SubscribAdmin(admin.ModelAdmin):
    list_display=['email','name','subscribed_on']
