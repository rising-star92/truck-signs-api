# Generated by Django 2.2.8 on 2021-07-21 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_order_amount_of_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='amount_of_product',
        ),
        migrations.AddField(
            model_name='productvariation',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]