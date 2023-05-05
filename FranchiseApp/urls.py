from django.urls import path
from FranchiseApp import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name= 'FranchiseApp'
urlpatterns = [
       #mits-healthacre url
       path('franchise/home/<int:pk>', views.HomeView.as_view(), name='home'),
       path('franchise/about/<int:pk>', views.AboutView.as_view(), name='about'),
       path('franchise/our_range/<int:pk>', views.OurRangeView.as_view(), name='Our_range'),
       path('franchise/contact/<int:pk>', views.ContactView.as_view(), name='Contact'),
       path('franchise/products/<int:pk>', views.ProductView.as_view(), name='Products'),
       path('franchise/product_detail/<int:pk>', views.ProductDetailView.as_view(), name='Productdetail'),
       path('send/',views.SendQuery.as_view(), name='send'),
     

]