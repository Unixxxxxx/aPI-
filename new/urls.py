from django.urls import path
from . import views

urlpatterns = [
    path('alpha/', views.alpha, name='alpha'),
]

