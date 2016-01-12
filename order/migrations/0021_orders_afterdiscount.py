# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_driverdetails_logistics'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='afterDiscount',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
