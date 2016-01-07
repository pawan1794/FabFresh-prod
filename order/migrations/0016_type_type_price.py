# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_auto_20160106_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='type_price',
            field=models.FloatField(default=0.0, max_length=100000),
        ),
    ]
