from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stocks")
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField()
    transactionType = models.IntegerField()

    def __str__(self):
        return '%s %s %d' % (self.date, ("Stock In" if self.transactionType > 0 else "Stock Out"), self.quantity)
    
