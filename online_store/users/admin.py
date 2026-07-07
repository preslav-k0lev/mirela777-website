from django.contrib import admin
from .models import User, UserAddress, Country

admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(Country)