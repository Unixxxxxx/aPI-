from django.contrib import admin
from .models import Product, VariationCategory, Variation

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [VariationInline]

admin.site.register(VariationCategory)

