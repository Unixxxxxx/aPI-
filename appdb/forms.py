from django import forms
from .models import Contact

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

