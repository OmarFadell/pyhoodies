from django.contrib import admin
from .models import Product, Category, ProductVariant, Drop

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductVariant)
admin.site.register(Drop)
