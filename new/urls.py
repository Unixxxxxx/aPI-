from django.urls import path 
from .import views 

urlpatterns = [
        path('',views.alpha,name='alpha'),
        ]
