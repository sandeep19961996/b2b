from django.core.mail import send_mail
from django.conf import settings
from AccountApp .models import User
from AccountApp .models import *
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
def send_forget_password_mail(email, token,id):
    id=urlsafe_base64_encode(force_bytes(id))
    subject ='Your forget Password Link'
    message=f'Hello {email}\n\n'f'We have received a request to reset the password for the PharmaXpert\n\n'  f'You can reset your password by clicking the link:\n' f'127.0.0.1:8000/account/change-password/{id}/{token}\n' f'If you did not request a new password. please let us know\n' f'immediately by replying to this email.\n\n'f'-The PharmaXpert team'
    email_form =settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message, email_form,recipient_list)
    return True
