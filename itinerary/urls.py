from django.urls import path 
from . import views

urlpatterns = [
        path('kedarnath', views.kedarnath, name='kedarnath'),
        ]
