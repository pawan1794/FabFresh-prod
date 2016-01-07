# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20160106_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_valid_until_time',
            field=models.DateTimeField(),
        ),
    ]
