from django.shortcuts import render
from .models import Product, Category


def index(request):
    # Вземаме всички активни продукти
    products = Product.objects.filter(is_active=True).prefetch_related('variants__media')
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/index.html', context)