from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Transaction
from .serializers import ProductSerializer, TransactionSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


