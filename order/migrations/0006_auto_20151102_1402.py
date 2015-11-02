# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20151021_0021'),
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
