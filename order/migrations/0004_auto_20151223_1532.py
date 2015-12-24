# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20151223_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statustimestamp',
            name='orders',
            field=models.ForeignKey(to='order.orders'),
        ),
    ]
