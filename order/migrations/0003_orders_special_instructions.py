# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orders_order_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='special_instructions',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
