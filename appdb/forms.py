from django import forms
from .models import Contact ,Enquiry 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter your email'
            }),
            'number': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter your phone number'
            }),
        }

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['first_name', 'last_name', 'work_email', 'mobile_number', 'enquiry_type', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'p-3 rounded-lg text-gray-800 w-full',
                'required': True
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'p-3 rounded-lg text-gray-800 w-full',
                'required': True
            }),
            'work_email': forms.EmailInput(attrs={
                'placeholder': 'Work Email',
                'class': 'p-3 rounded-lg text-gray-800 w-full',
                'required': True
            }),
            'mobile_number': forms.TextInput(attrs={
                'placeholder': 'Mobile Number',
                'class': 'p-3 rounded-lg text-gray-800 w-full',
                'required': True
            }),
            'enquiry_type': forms.Select(attrs={
                'class': 'p-3 rounded-lg text-gray-800 w-full',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Message',
                'class': 'p-3 rounded-lg text-gray-800 w-full md:col-span-2',
                'rows': 4
            }),
        }
