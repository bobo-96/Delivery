from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.FileField('Аватарка', upload_to='user_avatar/', null=True, blank=True)
    is_courier = models.BooleanField(default=False)
    date = models.DateTimeField(verbose_name='Дата Рождения', null=True, blank=True)


class Customer(models.Model):
    user = models.OneToOneField('user.User', models.CASCADE)
    balance = models.IntegerField(verbose_name='Баланс', null=True)


class Courier(models.Model):
    user = models.OneToOneField('user.User', models.CASCADE)





# Customer.objects.create(user=user)

