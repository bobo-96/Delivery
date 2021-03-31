from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user

        order = Order.objects.create(user=user, **validated_data)
        return order


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('status',)