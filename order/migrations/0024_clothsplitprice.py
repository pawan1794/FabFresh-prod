# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0023_orders_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothSplitPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeName', models.CharField(unique=True, max_length=100)),
                ('typeQuantity', models.IntegerField()),
                ('typePrice', models.FloatField(default=0.0, max_length=100000, validators=[django.core.validators.MinValueValidator(1)])),
                ('total', models.FloatField(default=0.0, max_length=100000, validators=[django.core.validators.MinValueValidator(1)])),
                ('orders', models.ForeignKey(related_name='ClothSplitPrice', to='order.orders')),
            ],
        ),
    ]
