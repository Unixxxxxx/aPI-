from django.shortcuts import render

# Create your views here.

def new(request):
    return render(request, 'nwe/new.html', {})
