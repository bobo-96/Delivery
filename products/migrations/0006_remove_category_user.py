# Generated by Django 3.1.7 on 2021-04-01 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_category_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
    ]
