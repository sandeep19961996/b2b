from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.emails import send_account_activation_email
from autoslug import AutoSlugField
from django.contrib.auth.models import AbstractUser
from AccountApp.city import STATE_CHOICES,cities
# class User(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Profile(BaseModel):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True , blank=True)
    profile_image = models.ImageField(upload_to = 'profile',null=True,blank=True)
    forget_password_token=models.CharField(max_length=100,null=True , blank=True)
   

    # def __str__(self):
    #     return self.user_id.str(uuid.uuid4())
@receiver(post_save , sender = User)
def  send_email_token(sender , instance , created , **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance , email_token = email_token)
            email = instance.email
            send_account_activation_email(email , email_token)

    except Exception as e:
        print(e)

# class NameCategory(models.Model):
#     name = models.CharField(max_length=40)
#     slug=AutoSlugField(populate_from='name',unique=True, null=True, default=None)

#     def __str__(self):
#         return self.name
# class NameDuretion(models.Model):
#     name = models.CharField(max_length=40)
#     slug=AutoSlugField(populate_from='name',unique=True, null=True, default=None)

#     def __str__(self):
#         return self.name
# class NameTime(models.Model):
#     name = models.CharField(max_length=40)
#     slug=AutoSlugField(populate_from='name',unique=True, null=True, default=None)

#     def __str__(self):
#         return self.name


# class PostRequirement(models.Model):
#     email=models.EmailField()
#     category=models.ForeignKey(NameCategory,related_name="category", on_delete=models.CASCADE,blank=True, null=True)
#     duretion=models.ForeignKey(NameDuretion,related_name="duretion", on_delete=models.CASCADE, blank=True, null=True)
#     time=models.ForeignKey(NameTime,related_name="time", on_delete=models.CASCADE, blank=True, null=True)
#     phone=models.CharField(max_length=12)
#     message=models.CharField(blank=True,max_length=500)

#     def __str__(self):
#      return self.email
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)  

CHOOSE_CATEGORY=(
                 ('Pharma Franchise','Pharma Franchise'),
                 ('Third Party Manufacturing','Third Party Manufacturing'),
                 ('Ayurvedic PCD Franchise','Ayurvedic PCD Franchise'),
                 ('Pharmaceutical Drugs and Medicine','Pharmaceutical Drugs and Medicine'),
                 ('Ayurvedic Herbal Manufacturing','Ayurvedic Herbal Manufacturing'),
                 ('Business Opportunities','Business Opportunities')
                    )

CHOOSE_DURETION=(
                 ('Immediate','Immediate'),
                 ('Within 15 Days','Within 15 Days'),
                 ('Within a Month','Within a Month')
                    )
CHOOSE_TIME=(
             ('Anytime','Anytime'),
             ('Morning','Morning'),
             ('Afternoon','Afternoon'),
             ('Evening','Evening')
             )


class PostRequirement(models.Model):
    email=models.EmailField()
    category=models.CharField(choices=CHOOSE_CATEGORY, max_length=100)
    duretion=models.CharField(choices=CHOOSE_DURETION, max_length=100)
    time=models.CharField(choices=CHOOSE_TIME,max_length=100)
    state=models.CharField(choices=STATE_CHOICES ,max_length=250)
    city=models.CharField(choices=cities,max_length=100)
    phone=models.CharField(max_length=12)
    message=models.CharField(blank=True,max_length=500)

    def __str__(self):
        return self.email