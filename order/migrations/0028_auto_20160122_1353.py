# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0027_clothsplitprice_invoiceid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_valid_until_time',
            field=models.DateTimeField(verbose_name=b'published'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_value_type',
            field=models.CharField(default=b'1', max_length=1, verbose_name=b'Type', choices=[(b'0', b'percentage'), (b'1', b'flat')]),
        ),
    ]
