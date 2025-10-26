# myapp/admin.py
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number')  # Columns to show in admin
    search_fields = ('name', 'email', 'number')  # Add search box
    list_filter = ('name',)  # Add filters if needed

