# Generated by Django 5.1.4 on 2025-01-08 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_feedbacks', to='products.colorvariant'),
        ),
    ]
