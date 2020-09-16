# Generated by Django 3.1 on 2020-09-17 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20200917_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalorder',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='historicalorder',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
