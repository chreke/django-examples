from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=16, unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
