# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20160106_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_valid_until_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 9, 7, 5, 271374, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
