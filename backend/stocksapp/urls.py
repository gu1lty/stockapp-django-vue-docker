from django.urls import path, include
from . import views
from rest_framework import routers

productRouter = routers.DefaultRouter()
productRouter.register('product', views.ProductView)

transactionRouter = routers.DefaultRouter()
productRouter.register('transaction', views.TransactionView)

urlpatterns = [
    path('', include(productRouter.urls)),
    path('transaction', include(transactionRouter.urls)),
]
