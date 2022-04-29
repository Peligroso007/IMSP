from django.db import models

class Payment(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    sales = models.ForeignKey('Sales', on_delete=models.CASCADE, null=True)
    now = models.BooleanField(default=True)


    def __str__(self):
        return self.product.product_name