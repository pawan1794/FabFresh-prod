# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20151223_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statustimestamp',
            name='orders',
        ),
        migrations.AddField(
            model_name='statustimestamp',
            name='order',
            field=models.ForeignKey(related_name='StatusTimeStamp', default=1, to='order.orders'),
            preserve_default=False,
        ),
    ]
