from django.db import models

class Sales(models.Model):
    grand_total = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)