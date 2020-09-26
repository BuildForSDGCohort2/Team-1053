# Generated by Django 3.1 on 2020-09-21 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20200918_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalorderitem',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalorderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='historicaltracking',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicaltracking',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='tracking',
            name='status',
        ),
        migrations.RemoveField(
            model_name='tracking',
            name='tracking_number',
        ),
        migrations.AddField(
            model_name='order',
            name='expected_delivery',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 16, 32, 45, 317952), null=True),
        ),
        migrations.AddField(
            model_name='tracking',
            name='event',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tracking',
            name='event_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='HistoricalOrder',
        ),
        migrations.DeleteModel(
            name='HistoricalOrderItem',
        ),
        migrations.DeleteModel(
            name='HistoricalTracking',
        ),
    ]
