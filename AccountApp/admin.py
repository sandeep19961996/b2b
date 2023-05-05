from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from AccountApp .models import *
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['user_id','user','is_email_verified','email_token','profile_image','forget_password_token']


# @admin.register(NameCategory)
# class NameCategoryAdmin(admin.ModelAdmin):
#     list_display=['name','slug']

# @admin.register(NameDuretion)
# class NameDuretionAdmin(admin.ModelAdmin):
#     list_display=['name','slug']

# @admin.register(NameTime)
# class NameDuretionAdmin(admin.ModelAdmin):
#     list_display=['name','slug']

@admin.register(PostRequirement)
class PostRequirmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['email','category','duretion','state','city','time','phone','message']