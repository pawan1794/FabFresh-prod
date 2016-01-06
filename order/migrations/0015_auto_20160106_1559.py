# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20160106_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponType',
            fields=[
                ('coupon_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('coupon_type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_coupon_type',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'0', b'firstorder'), (b'1', b'flatoff'), (b'2', b'one time use')]),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_tag',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
