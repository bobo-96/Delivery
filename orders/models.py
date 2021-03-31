from django.db import models


class Order(models.Model):
    ORDER_STATUS = (
        ('Pending', 'Pending'),
        ('OnWay', 'Order on way'),
        ('Delivered', 'Order delivered'),
    )
    status = models.CharField(max_length=10, choices=ORDER_STATUS)
    quantity = models.IntegerField(verbose_name='количество продуктов')
    total_price = models.DecimalField(max_digits=100000, decimal_places=2)
    category = models.ForeignKey('products.Category', models.CASCADE, 'order_category', null=True)
    product = models.ForeignKey('products.Product', models.CASCADE, 'order_product')
    user = models.ForeignKey('user.User', models.CASCADE, 'order_user', null=True)

