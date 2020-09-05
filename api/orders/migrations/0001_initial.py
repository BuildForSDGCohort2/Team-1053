# Generated by Django 3.1 on 2020-09-05 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20200905_1607'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('On Hold', 'On Hold'), ('Confirmed', 'Confirmed'), ('Canceled', 'Canceled'), ('Abandoned Cart', 'Abandoned Cart')], default='New', max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('Packed', 'Packed'), ('Dispatched', 'Dispatched'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], default='Processing', max_length=200, null=True)),
                ('location', models.CharField(default='WareHouse', max_length=200)),
                ('delivery_date', models.DateTimeField()),
                ('ship_to', models.CharField(max_length=255, null=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.IntegerField(null=True)),
                ('price', models.FloatField(default=0.0)),
                ('order', models.ManyToManyField(to='orders.Order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalTracking',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('tracking_number', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('Packed', 'Packed'), ('Dispatched', 'Dispatched'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], default='Processing', max_length=200, null=True)),
                ('location', models.CharField(default='WareHouse', max_length=200)),
                ('delivery_date', models.DateTimeField()),
                ('ship_to', models.CharField(max_length=255, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='orders.order')),
            ],
            options={
                'verbose_name': 'historical tracking',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalOrderItem',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('product_quantity', models.IntegerField(null=True)),
                ('price', models.FloatField(default=0.0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventory.product')),
            ],
            options={
                'verbose_name': 'historical order item',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalOrder',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('code', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('On Hold', 'On Hold'), ('Confirmed', 'Confirmed'), ('Canceled', 'Canceled'), ('Abandoned Cart', 'Abandoned Cart')], default='New', max_length=200, null=True)),
                ('date_created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('customer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.customer')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical order',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]