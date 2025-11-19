from django.shortcuts import render

# Create your views here.

def alpha(request):
    return render(request,"alpha.html",{})
