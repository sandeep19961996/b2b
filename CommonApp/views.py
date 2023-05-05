from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import View
from B2bApp .models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate , login , logout
from django.urls import reverse
# Create your views here.

#error page function
def Error_404(request):
    return render(request,'error/error_404.html')

