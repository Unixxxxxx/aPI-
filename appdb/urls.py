from django.urls import path 
from . import views

urlpatterns = [
        path('', views.contact_view, name='contact'),
        path('new/', views.new, name= 'new'),
        path('index/', views.index, name='index'),
        path('enquiry/', views.Enquiry_view, name='enquiry'),
        path('success/', views.success_view, name='success'),
        path('services/', views.services_view, name='services'),
        ]
