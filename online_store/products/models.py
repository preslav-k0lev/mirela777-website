from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name


class Discount(models.Model):
    promocode = models.CharField(max_length=50, unique=True)
    is_percent = models.BooleanField(default=False, help_text="True = as %, False = as money")
    value = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_for_whole_order = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.promocode} ({self.value}{'%' if self.is_percent else ' BGN'})"


class Product(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    material = models.CharField(max_length=255, blank=True, null=True)
    pillow_cases = models.IntegerField(default=0, help_text="Number of pillow cases included")

    # META DATA
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True, help_text="Comma-separated tags")

    # CONTROL
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # RELATIONS
    discounts = models.ManyToManyField(Discount, blank=True, related_name='products')

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    size = models.CharField(max_length=50)
    sku = models.CharField(max_length=100, unique=True)

    # FINANCIALS
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cogs_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cost of Goods Sold")

    # INVENTORY
    quantity = models.PositiveIntegerField(default=0)
    is_in_stock = models.BooleanField(default=True)
    low_stock_threshold = models.PositiveIntegerField(default=5)

    # LOGISTICS
    weight = models.DecimalField(max_digits=6, decimal_places=2, help_text="Weight in kg", blank=True, null=True)
    dimensions = models.CharField(max_length=100, help_text="e.g., 200x220x10", blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} - {self.size} ({self.sku})"


class ProductMedia(models.Model):
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='media')
    address = models.URLField(max_length=500, help_text="Image or video URL")
    is_main = models.BooleanField(default=False)
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Product Media"

    def __str__(self):
        return f"Media for {self.product_variant.sku} - {'Main' if self.is_main else 'Secondary'}"