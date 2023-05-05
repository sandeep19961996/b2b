from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class WebsiteLogo (models.Model):
    logo_image=models.ImageField(upload_to="websitelogo")
    def delete(self,*args, **kwargs):
        self.logo_image.delete()
        return super(WebsiteLogo, self).delete(*args, **kwargs)

    def Logo_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.logo_image.url))
    Logo_image.short_description ='logo_image'
    Logo_image.allow_tag =True