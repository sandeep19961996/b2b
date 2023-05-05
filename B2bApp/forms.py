from django import forms
from django.core.mail import send_mail
from django.conf import settings
from B2bApp . models import *
# from tinymce.widgets import TinyMCE
from django.forms import MultiWidget, TextInput

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': "form-control " }))
    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    subject=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': "form-control"}))
    message=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows':4,'class': "form-control" }))
    # captcha = CaptchaField()
    

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        cl_data =super().clean()

        # Cleaned data
        cl_data = self.clean()
        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')
        
        msg = f'hi {name},'
        msg += f'\n"{from_email}"\n\n'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg
  

    def send(self):
        # send email using the self.cleaned_data dictionary
        
        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email', 'name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Subscriber.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already subscribed.')
        return email

