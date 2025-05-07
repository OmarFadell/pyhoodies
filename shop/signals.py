from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import ProductVariant, Product
from django.db import models
from django.db.models import Sum

def update_product_stock(product):
    total_stock = product.variants.aggregate(total=models.Sum('stock'))['total'] or 0
    product.stock = total_stock
    product.save(update_fields=['stock'])

@receiver(post_save, sender=ProductVariant)
def update_stock_on_save(sender, instance, **kwargs):
    update_product_stock(instance.product)

@receiver(post_delete, sender=ProductVariant)
def update_stock_on_delete(sender, instance, **kwargs):
    update_product_stock(instance.product)


