from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('master/<slug:category_slug>/', views.category_master_detail, name='category_master_detail'),
    path('about/', views.about, name='about'),

]
