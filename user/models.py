from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE)
    balance = models.IntegerField(verbose_name='Баланс')
    date = models.DateTimeField(verbose_name='Дата Рождения')


class Courier(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE)


class Stuff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE)



