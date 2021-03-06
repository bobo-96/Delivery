# Generated by Django 3.1.7 on 2021-03-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('InStock', 'Order in stock'), ('OnWay', 'Order on way'), ('Delivered', 'Order delivered')], max_length=10)),
                ('quantity', models.IntegerField(verbose_name='количество продуктов')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=100000)),
            ],
        ),
    ]
