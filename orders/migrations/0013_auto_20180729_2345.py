# Generated by Django 2.0.7 on 2018-07-29 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20180729_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='item_pasta',
            new_name='pasta',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='item_pizza',
            new_name='pizza',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='item_pizzatopping',
            new_name='pizzatopping',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='item_platter',
            new_name='platter',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='item_salad',
            new_name='salad',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='item_sub',
            new_name='sub',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='item_subtopping',
            new_name='subtopping',
        ),
    ]