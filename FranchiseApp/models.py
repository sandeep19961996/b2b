from django.db import models
from django.utils.safestring import mark_safe
from autoslug import AutoSlugField
from B2bApp .models import *
# Create your models here.


    
class Send(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=False)
    phone=models.CharField(max_length=14)
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
class MitsProducts(models.Model):
    company=models.ForeignKey(CompanyInfo,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name',unique=True, null=True, default=None)
    pro_image=models.ImageField(upload_to="mitsproductimage")
    description=models.TextField(max_length=500)
    packing=models.CharField(max_length=100)
    tags=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['name']
    
    
    def delete(self,*args, **kwargs):
        self.pro_image.delete()
        return super(MitsProducts, self).delete(*args, **kwargs)

    def pro_images(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.pro_image.url))
    pro_images.short_description ='pro_image'
    pro_images.allow_tag =True

# class ShineProducts(models.Model):
#     name=models.CharField(max_length=100)
#     slug = AutoSlugField(populate_from='name',unique=True, null=True, default=None)
#     pro_image=models.ImageField(upload_to="shineproductimage")
#     description=models.TextField(max_length=500)
#     packing=models.CharField(max_length=100)
#     tags=models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name
#     class Meta:
#         ordering=['name']
#     def delete(self,*args, **kwargs):
#         self.pro_image.delete()
#         return super(ShineProducts, self).delete(*args, **kwargs)

#     def pro_images(self):
#         return mark_safe('<img src="{}" width="100" />'.format(self.pro_image.url))
#     pro_images.short_description ='pro_image'
#     pro_images.allow_tag =True

# class EdmundProducts(models.Model):
#     name=models.CharField(max_length=100)
#     slug = AutoSlugField(populate_from='name',unique=True, null=True, default=None)
#     pro_image=models.ImageField(upload_to="edmundproductimage")
#     description=models.TextField(max_length=500)
#     packing=models.CharField(max_length=100)
#     tags=models.CharField(max_length=100)
   

#     def __str__(self):
#         return self.name
#     class Meta:
#         ordering=['name']

#     def delete(self,*args, **kwargs):
#         self.pro_image.delete()
#         return super(EdmundProducts, self).delete(*args, **kwargs)

#     def pro_images(self):
#         return mark_safe('<img src="{}" width="100" />'.format(self.pro_image.url))
#     pro_images.short_description ='pro_image'
#     pro_images.allow_tag =True

    
# class MedFenseProducts(models.Model):
#     name=models.CharField(max_length=100)
#     slug = AutoSlugField(populate_from='name',unique=True, null=True, default=None)
#     pro_image=models.ImageField(upload_to="medfensseproductimage")
#     description=models.TextField(max_length=500)
#     packing=models.CharField(max_length=100)
#     tags=models.CharField(max_length=100)
  
#     def __str__(self):
#         return self.name
#     class Meta:
#         ordering=['name']

#     def delete(self,*args, **kwargs):
#         self.pro_image.delete()
#         return super(MedFenseProducts, self).delete(*args, **kwargs)

#     def pro_images(self):
#         return mark_safe('<img src="{}" width="100" />'.format(self.pro_image.url))
#     pro_images.short_description ='pro_image'
#     pro_images.allow_tag =True

# class RapidProducts(models.Model):
#     name=models.CharField(max_length=100)
#     slug = AutoSlugField(populate_from='name',unique=True, null=True, default=None)
#     pro_image=models.ImageField(upload_to="rapidproductimage")
#     description=models.TextField(max_length=500)
#     packing=models.CharField(max_length=100)
#     tags=models.CharField(max_length=100)
 
#     def __str__(self):
#         return self.name
#     class Meta:
#         ordering=['name']

#     def delete(self,*args, **kwargs):
#         self.pro_image.delete()
#         return super(RapidProducts, self).delete(*args, **kwargs)

#     def pro_images(self):
#         return mark_safe('<img src="{}" width="100" />'.format(self.pro_image.url))
#     pro_images.short_description ='pro_image'
#     pro_images.allow_tag =True

# class ServoProducts(models.Model):
#     name=models.CharField(max_length=100)
#     slug = AutoSlugField(populate_from='name',unique=True, null=True, default=None)
#     pro_image=models.ImageField(upload_to="servoproductimage")
#     description=models.TextField(max_length=500)
#     packing=models.CharField(max_length=100)
#     tags=models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
#     class Meta:
#         ordering=['name']

#     def delete(self,*args, **kwargs):
#         self.pro_image.delete()
#         return super(ServoProducts, self).delete(*args, **kwargs)

#     def pro_images(self):
#         return mark_safe('<img src="{}" width="100" />'.format(self.pro_image.url))
#     pro_images.short_description ='pro_image'
#     pro_images.allow_tag =True

# class RonishProducts(models.Model):
#     name=models.CharField(max_length=100)
#     slug = AutoSlugField(populate_from='name',unique=True, null=True, default=None)
#     pro_image=models.ImageField(upload_to="ronishproductimage")
#     description=models.TextField(max_length=500)
#     packing=models.CharField(max_length=100)
#     tags=models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
#     class Meta:
#         ordering=['name']

#     def delete(self,*args, **kwargs):
#         self.pro_image.delete()
#         return super(RonishProducts, self).delete(*args, **kwargs)

#     def pro_images(self):
#         return mark_safe('<img src="{}" width="100" />'.format(self.pro_image.url))
#     pro_images.short_description ='pro_image'
#     pro_images.allow_tag =True