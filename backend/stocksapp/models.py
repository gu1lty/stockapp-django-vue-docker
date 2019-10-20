from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50)
    quatity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    transactionType = models.IntegerField()
