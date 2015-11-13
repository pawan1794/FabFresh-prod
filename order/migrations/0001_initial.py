# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothInfo',
            fields=[
                ('cloth_id', models.AutoField(serialize=False, primary_key=True)),
                ('gender', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('color_id', models.AutoField(serialize=False, primary_key=True)),
                ('color_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DriverDetails',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('driver_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('order_id', models.CharField(max_length=20, null=True, blank=True)),
                ('delivery_id', models.CharField(max_length=20, null=True, blank=True)),
                ('new_trip', models.BooleanField()),
                ('driver_name', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('amount', models.FloatField(null=True, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('weight', models.FloatField(null=True, blank=True)),
                ('created_at_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default=b'1', max_length=1, choices=[(b'0', b'cancelled'), (b'1', b'created'), (b'2', b'wash'), (b'3', b'dry'), (b'4', b'iron'), (b'5', b'processComplete'), (b'6', b'shipRequest'), (b'7', b'shipped'), (b'8', b'completed')])),
                ('order_type', models.CharField(max_length=10, null=True, blank=True)),
                ('special_instructions', models.CharField(max_length=200, null=True, blank=True)),
                ('p_id', models.IntegerField(null=True, blank=True)),
                ('delivery_id', models.CharField(max_length=200, null=True, blank=True)),
                ('roadrunner_order_id', models.CharField(max_length=200, null=True, blank=True)),
                ('owner', models.ForeignKey(related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('size_id', models.AutoField(serialize=False, primary_key=True)),
                ('size_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_id', models.AutoField(serialize=False, primary_key=True)),
                ('type_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='driverdetails',
            name='orders',
            field=models.ForeignKey(to='order.orders'),
        ),
        migrations.AddField(
            model_name='clothinfo',
            name='color',
            field=models.ForeignKey(to='order.Color'),
        ),
        migrations.AddField(
            model_name='clothinfo',
            name='order',
            field=models.ForeignKey(to='order.orders'),
        ),
        migrations.AddField(
            model_name='clothinfo',
            name='size',
            field=models.ForeignKey(to='order.Size'),
        ),
        migrations.AddField(
            model_name='clothinfo',
            name='type',
            field=models.ForeignKey(to='order.Type'),
        ),
    ]
