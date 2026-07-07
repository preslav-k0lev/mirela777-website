from django.contrib import admin
from .models import Product, ProductMedia, ProductVariant, Discount, Category

admin.site.register(Product)
admin.site.register(ProductMedia)
admin.site.register(ProductVariant)
admin.site.register(Discount)
admin.site.register(Category)