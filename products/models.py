from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=255)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    customer = models.ForeignKey('user.Customer', models.CASCADE, 'product_customer')
    courier = models.ForeignKey('user.Courier', models.CASCADE, 'product_courier')
    stuff = models.ForeignKey('user.Stuff', models.CASCADE, 'product_stuff')

