from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name


class Drop(models.Model):
    name=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()  
    image_url = models.URLField(max_length=500,default="https://example.com/default.jpg")
    price = models.DecimalField(max_digits=8, decimal_places=2) 
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, null=True, blank=True)
    # stock = models.IntegerField(null=True, blank=True)  
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    SIZE_CHOICES = [ ('S','Small'), ('M','Medium'), ('L','Large'), ('XL','Extra Large') ]
    COLOR_CHOICES = [ ('W','White'), ('R','RED'), ('B','Blue'), ('BL','BLACK'),('G','GREY') ]

    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M')
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='BL')
    stock = models.IntegerField()

    class Meta:
        unique_together = ('product', 'size', 'color')

    def __str__(self):
        return f"{self.product.name} - {self.size} - {self.color}"