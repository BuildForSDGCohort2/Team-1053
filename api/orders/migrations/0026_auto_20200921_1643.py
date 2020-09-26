# Generated by Django 3.1 on 2020-09-21 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20200921_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracking',
            name='order',
        ),
        migrations.AddField(
            model_name='tracking',
            name='order_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='expected_delivery',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 16, 43, 0, 805740), null=True),
        ),
    ]
