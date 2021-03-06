# Generated by Django 2.0.7 on 2018-07-28 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20180728_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Pizza Type',
                'verbose_name_plural': 'Pizza Types',
            },
        ),
        migrations.RemoveField(
            model_name='dinnerplatter',
            name='category',
        ),
        migrations.AddField(
            model_name='dinnerplatter',
            name='size_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dinnerplattersizes', to='orders.SizeCategory'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='pizza_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pizzatypes', to='orders.PizzaCategory'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='size_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pizzasizes', to='orders.SizeCategory'),
        ),
    ]
