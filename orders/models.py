from django.db import models


class Order(models.Model):
    ORDER_STATUS = (
        ('InStock', 'Order in stock'),
        ('OnWay', 'Order on way'),
        ('Delivered', 'Order delivered'),
    )
    status = models.CharField(max_length=10, choices=ORDER_STATUS)
    quantity = models.IntegerField(verbose_name='количество продуктов')
    total_price = models.DecimalField(max_digits=100000, decimal_places=2)
    product = models.ForeignKey('products.Product', models.CASCADE, 'order_product')
    customer = models.ForeignKey('user.Customer', models.CASCADE, 'order_customer')
    courier = models.ForeignKey('user.Courier', models.CASCADE, 'order_courier')
    stuff = models.ForeignKey('user.Stuff', models.CASCADE, 'order_stuff')

