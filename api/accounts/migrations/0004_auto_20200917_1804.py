# Generated by Django 3.1 on 2020-09-17 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200917_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='street',
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]