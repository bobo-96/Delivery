from django.shortcuts import render


from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import Order
from orders.permissions import IsOrderOwnerOrReadOnly, IsStatusOwnerOrReadOnly

from orders.serializers import OrderSerializer, StatusSerializer


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'
    permission_classes = (IsOrderOwnerOrReadOnly,)


class StatusView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'pk'
    permission_classes = (IsStatusOwnerOrReadOnly,)