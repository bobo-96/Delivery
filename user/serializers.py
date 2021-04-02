from rest_framework import serializers

from orders.models import Order
from user.models import User, Customer
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'date', 'password', 'username', 'avatar'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    # def to_representation(self, instance):
    #     ret = super(StorySerializer, self).to_representation(instance)
    #     # check the request is list view or detail view
    #     is_list_view = isinstance(self.instance, list)
    #     extra_ret = {'key': 'list value'} if is_list_view else {'key': 'single value'}
    #     ret.update(extra_ret)
    #     return ret

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        token, _ = Token.objects.get_or_create(user=user)
        Customer.objects.create(user=user)
        validated_data['token'] = token.key
        print('-'*80)
        print(validated_data)
        return validated_data


class OrdersForUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'status', 'quantity', 'total_price', 'category', 'product')


class ProfileSerializer(serializers.ModelSerializer):
    order_user = OrdersForUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('avatar', 'username', 'first_name', 'last_name', 'email', 'order_user')
