from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=50, null=True, blank=True)
    product_type = models.CharField(max_length=20, null=True, blank=True)
    product_marked_price = models.IntegerField(null=True, blank=True)
    product_discount = models.IntegerField(null=True, blank=True)
    product_buying_price = models.IntegerField(null=True, blank=True)
    product_stock = models.IntegerField(null=True, blank=True)


    product_experies = models.DateTimeField(null=True, blank=True)
    product_manufacture = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.product_name