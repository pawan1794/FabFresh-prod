# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0025_auto_20160115_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothsplitprice',
            name='afterDiscount',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='clothsplitprice',
            name='amount',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='clothsplitprice',
            name='created_at_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
