from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    weight = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    inStock = models.BooleanField

    # name, description, weight, price, cost (to seller), and category
