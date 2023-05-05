from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from FranchiseApp .models import *




@admin.register(Send)
class SendQueryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['name','email','phone','message']

@admin.register(MitsProducts)
class Mitsadmin(admin.ModelAdmin):
  list_display=['name','slug','pro_images','tags','description','packing']
  readonly_fields = ['pro_images']
  search_fields=['name','tags','packing']