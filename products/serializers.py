from rest_framework import serializers

from products.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user

        category = Category.objects.create(user=user, **validated_data)
        return category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user

        product = Product.objects.create(user=user, **validated_data)
        return product


