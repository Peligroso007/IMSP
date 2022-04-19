from django.db import models

class Payment(models.Model):
    sales = models.ForeignKey('Sales', on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.product.product_name