# Generated by Django 5.1.4 on 2025-01-06 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_colorvariant_color_name_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('succeeded', 'Succeeded')], default='pending', max_length=20),
        ),
    ]
