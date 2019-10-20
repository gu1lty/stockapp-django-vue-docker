from rest_framework import serializers
from .models import Product, Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('product', 'quantity', 'date', 'transactionType',)

    def validate_quantity(self, value):
        data = self.get_initial()
        pID = int(data.get('product'))
        tType = int(data.get('transactionType'))
        p = Product.objects.get(id=pID)
        if tType < 1:
            if p.quantity < value:
                raise serializers.ValidationError("Quantity Exceeds Current Stock")
        p.save()
        return value

    def create(self, validated_data):
        prod = validated_data.pop('product')
        pID = prod.id
        tType = validated_data['transactionType']
        tQuantity = validated_data['quantity']
        p = Product.objects.get(id=pID)
        if tType < 1:
            p.quantity -= tQuantity
        else:
            p.quantity += tQuantity
        p.save()
        t = Transaction(**validated_data)
        t.product = p
        t.save()
        return t

class ProductSerializer(serializers.ModelSerializer):
    stocks = serializers.SerializerMethodField()

    def get_stocks(self, obj):
        stocks = Transaction.objects.order_by('-date')[:10]
        return TransactionSerializer(stocks, many=True).data
        
    class Meta:
        model = Product
        fields = ('name', 'sku', 'quantity', 'stocks',)
