from rest_framework import serializers

from orders.models import Order
from user.models import User


class OrdersForUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'status', 'quantity', 'total_price', 'category', 'product')


class UserSerializer(serializers.ModelSerializer):
    order_user = OrdersForUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('avatar', 'username', 'first_name', 'last_name', 'email', 'order_user')
