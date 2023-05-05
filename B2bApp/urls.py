from django.urls import path
from B2bApp import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name= 'B2bApp'
urlpatterns = [
              path('', views.HomeView.as_view(), name='home'),
              path('serach/', views.Serach.as_view(), name='serach'),
  ##############################   parties all views ########################################
              path('about/', views.AboutView.as_view(), name='about'),
              path('contact/', views.ContactView.as_view(), name='contact'),
              path('category/', views.CategoryView.as_view(), name='category'),
              path('listing/', views.ListingView.as_view(), name='listing'),
              path('success/', views.ContactSuccessView.as_view(), name="success"),
              path('filter-category/', views.FilterCategory.as_view(), name='filter_cate'),
              path('filter-category/<int:id>/', views.FilterCate.as_view(), name='cate_filter' ),
              path('filter-location/<str:loc>/', views.Filterlocation.as_view(), name='location_filter' ),
              path('filter-subcategory/<int:id>/', views.FilterSubcategory.as_view(), name='filter_subcategory' ),
              path('send/',views.SendQuery.as_view(), name='send'),
              path('subscribe/',views.subscribe ,name='subscribe')
  ##############################  end parties all views ######################################
]