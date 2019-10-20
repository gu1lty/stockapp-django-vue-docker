from rest_framework import serializers
from .models import Product, Transaction

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'sku', 'quantity')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('product', 'quantity', 'date', 'transactionType')