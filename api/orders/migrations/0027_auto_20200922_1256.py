# Generated by Django 3.1 on 2020-09-22 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_auto_20200921_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expected_delivery',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 26, 12, 56, 23, 257701), null=True),
        ),
    ]
