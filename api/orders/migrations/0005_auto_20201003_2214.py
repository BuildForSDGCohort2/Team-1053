# Generated by Django 3.1 on 2020-10-03 22:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20201003_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='expected_delivery',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 7, 22, 14, 54, 666261), null=True),
        ),
    ]
