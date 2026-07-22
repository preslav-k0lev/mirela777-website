# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="In percents [example: 20.00]")

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class User(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')


    # Email for logins
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email


class UserAddress(models.Model):
    # asd field is automatically asd_id when using FK
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    delivery_address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "User Addresses"

    def __str__(self):
        return f"{self.delivery_address}, {self.city}"