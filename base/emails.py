import imp
from AccountApp .models import *
from django.conf import settings
from django.core.mail import send_mail



def send_account_activation_email(email,email_token):
 
 subject = 'Your account needs to be verified'
 email_from = settings.EMAIL_HOST_USER
 message = f'Hi [name]\n\n' f'We are happy you signed up for  PharmaXpert \n\n' f'Verify your email address http://127.0.0.1:8000/account/activate/{email_token}/\n\n\n' f'Thanks! The PharmaXpert team\n\n'
 send_mail(subject , message , email_from , [email])


