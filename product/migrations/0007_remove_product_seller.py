# Generated by Django 4.2.3 on 2023-07-30 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
    ]
