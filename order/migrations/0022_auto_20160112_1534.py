# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_orders_afterdiscount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_used_counter',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
