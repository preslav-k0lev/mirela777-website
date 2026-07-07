from django.contrib import admin
from .models import Order, OrderProductVariant

admin.site.register(Order)
admin.site.register(OrderProductVariant)