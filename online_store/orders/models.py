from django.db import models
from django.conf import settings


class Order(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    class Status(models.TextChoices):
        PENDING = 'pending', 'Очаква се'
        PROCESSING = 'processing', 'Обработва се'
        SHIPPED = 'shipped', 'Изпратена'
        DELIVERED = 'delivered', 'Доставена'
        CANCELLED = 'cancelled', 'Отказана'

    # CORE
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # FINANCIAL DATA
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2, default=20.00)  # 20% Bulgaria
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    promocode = models.CharField(max_length=50, blank=True, null=True)
    total_discount_for_purchase = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # LOGISTICS
    tracking_number = models.CharField(max_length=100, blank=True, null=True)

    # PAYMENT PROCESSING
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    payment_status = models.CharField(max_length=50, default='unpaid')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.id} by {self.user}"


class OrderProductVariant(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )


    product_variant = models.ForeignKey(
        'products.ProductVariant',
        on_delete=models.SET_NULL,
        null=True
    )


    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Variant {self.product_variant_id} for Order #{self.order_id}"