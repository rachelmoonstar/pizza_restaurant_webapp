# Generated by Django 2.0.7 on 2018-07-31 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_auto_20180731_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
