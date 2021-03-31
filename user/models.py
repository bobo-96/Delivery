from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.FileField('Аватарка', upload_to='user_avatar/')


class Customer(models.Model):
    user = models.OneToOneField('user.User', models.CASCADE)
    balance = models.IntegerField(verbose_name='Баланс')
    date = models.DateTimeField(verbose_name='Дата Рождения')


class Courier(models.Model):
    user = models.OneToOneField('user.User', models.CASCADE)






