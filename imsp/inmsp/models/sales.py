from django.db import models

class Sales(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)

    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    profit = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product.product_name