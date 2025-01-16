# Generated by Django 5.1.4 on 2025-01-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.CharField(blank=True, choices=[('in_stock', 'В наличии'), ('out_of_stock', 'Нет в наличии')], default='in_stock', max_length=20, null=True),
        ),
    ]