# Generated by Django 5.1.4 on 2025-01-14 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_product_orderitem_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='products',
        ),
    ]
