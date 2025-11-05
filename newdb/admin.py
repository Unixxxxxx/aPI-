from django.contrib import admin
from .models import Newdb

@admin.register(Newdb)
class NewdbAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')   # columns shown in admin list view
    search_fields = ('name', 'email')         # adds a search box

