from django.contrib import admin
from CommonApp .models import *
# Register your models here.
@admin.register(WebsiteLogo)
class LogoAdmin (admin.ModelAdmin):
     list_display=['Logo_image']
     readonly_fields=['Logo_image']