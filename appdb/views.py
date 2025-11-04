from django.shortcuts import render, redirect 
from .models import Service
from .forms import ContactForm, EnquiryForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def services_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})
def index(request):
    return render(request, 'index.html', {})

def Enquiry_view(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EnquiryForm()
    return render(request, 'enquiry.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')
