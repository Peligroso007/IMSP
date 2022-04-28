from django.db import models

class Stock(models.Model):
    suppliers = models.ForeignKey('Suppliers', on_delete=models.CASCADE, null=True)

    quantity_remaining = models.IntegerField(null=True, blank=True)
    quantity_imported = models.IntegerField(null=True, blank=True)
    quantity_sold = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.product.product_name