# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20151229_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coupon_tag', models.CharField(max_length=100)),
                ('coupon_created_at_time', models.DateTimeField(auto_now_add=True)),
                ('coupon_valid_until_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('coupon_used_counter', models.IntegerField(null=True, blank=True)),
                ('coupon_value_type', models.CharField(default=b'1', max_length=1, choices=[(b'0', b'percentage'), (b'1', b'flat')])),
                ('coupon_value', models.IntegerField()),
                ('coupon_valid_flag', models.BooleanField()),
                ('coupon_coupon_type', models.CharField(default=b'1', max_length=1, choices=[(b'0', b'firstorder'), (b'1', b'flatoff')])),
            ],
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='color',
            name='color_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='size',
            name='size_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='type',
            name='type_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='coupon',
            field=models.ForeignKey(blank=True, to='order.Coupon', null=True),
        ),
    ]
