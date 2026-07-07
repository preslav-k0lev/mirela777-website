from django.db import models
from django.conf import settings
# Ако нямаш потребителски ап, Django използва вградения: settings.AUTH_USER_MODEL
# Ако твоят потребителски модел е в ап наречен 'users', можеш да го реферираш като 'users.User'

class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='carts'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} - User: {self.user.email if hasattr(self.user, 'email') else self.user.username}"


class CartProductVariant(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='cart_items'
    )

    product_variant = models.ForeignKey(
        'products.ProductVariant',
        on_delete=models.CASCADE,
        related_name='in_carts'
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:

        verbose_name_plural = "Cart Product Variants"
        unique_together = ('cart', 'product_variant')

    def __str__(self):
        return f"{self.quantity}x {self.product_variant} in Cart {self.cart.id}"