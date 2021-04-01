from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from products.models import Product, Category
from products.permissions import IsProductOwnerOrReadOnly
from products.serializers import ProductSerializer, CategorySerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    permission_classes = (IsProductOwnerOrReadOnly,)


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = (IsProductOwnerOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['price', 'category']





