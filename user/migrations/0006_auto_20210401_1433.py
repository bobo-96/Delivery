# Generated by Django 3.1.7 on 2021-04-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210401_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(null=True, verbose_name='Баланс'),
        ),
    ]
