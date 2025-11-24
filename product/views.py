from django.shortcuts import render, get_object_or_404
from .models import Product, Variation

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    variations = product.variations.all()
    return render(request, 'product_detail.html', {
        'product': product,
        'variations': variations,
    })

