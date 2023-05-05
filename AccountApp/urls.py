from django.urls import path
from AccountApp import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name= 'AccountApp'
urlpatterns = [
       path('post/', views.PosttView.as_view(), name='post'),
       path('success/', views.ContactSuccessView.as_view(), name="success_pro"),
       path('login/', views.login_page, name='login'),
       path('signup/', views.register_page, name='signup'),
       path('logout/',views.UserLogoutView.as_view(),name='logout'),
       path('activate/<email_token>/' , views.activate_email , name="activate_email"),

      # Passsword reset url
      path('forget-password/',views.forgetpassword,name="forget_password"),
      path('change-password/<token>/<str:id>',views.changepassword,name="change_password"),
      
]