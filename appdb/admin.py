from django.contrib import admin
from .models import Contact, Service , Enquiry 

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number')  # Columns to show in admin
    search_fields = ('name', 'email', 'number')  # Add search box
    list_filter = ('name',)  # Add filters if needed

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'button_text')

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'work_email', 'mobile_number', 'enquiry_type', 'submitted_at')
    list_filter = ('enquiry_type', 'submitted_at')
    search_fields = ('first_name', 'last_name', 'work_email', 'mobile_number')
    ordering = ('-submitted_at',)
