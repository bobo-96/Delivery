from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории',max_length=255)
    user = models.ForeignKey('user.User', models.CASCADE, 'user_category', null=True)


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=255)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    category = models.ForeignKey('products.Category', models.CASCADE, 'product_category', null=True)
    user = models.ForeignKey('user.User', models.CASCADE, 'user_product', null=True)


