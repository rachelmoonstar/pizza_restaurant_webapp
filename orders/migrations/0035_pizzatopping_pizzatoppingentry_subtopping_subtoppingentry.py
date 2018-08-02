# Generated by Django 2.0.7 on 2018-08-01 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0034_menu_topping'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaTopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Pizza Topping',
                'verbose_name_plural': 'Pizza Toppings',
            },
        ),
        migrations.CreateModel(
            name='PizzaToppingEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderentry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.OrderEntry')),
                ('topping1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topping1', to='orders.PizzaTopping')),
                ('topping2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topping2', to='orders.PizzaTopping')),
                ('topping3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topping3', to='orders.PizzaTopping')),
            ],
        ),
        migrations.CreateModel(
            name='SubTopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Sub Topping',
                'verbose_name_plural': 'Sub Toppings',
            },
        ),
        migrations.CreateModel(
            name='SubToppingEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderentry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.OrderEntry')),
                ('topping1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topping1', to='orders.SubTopping')),
                ('topping2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topping2', to='orders.SubTopping')),
                ('topping3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topping3', to='orders.SubTopping')),
                ('topping4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topping4', to='orders.SubTopping')),
            ],
        ),
    ]