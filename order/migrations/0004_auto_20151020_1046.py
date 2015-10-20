# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_orders_special_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'0', b'cancelled'), (b'1', b'created'), (b'2', b'wash'), (b'3', b'dry'), (b'4', b'iron'), (b'5', b'complete'), (b'6', b''), (b'7', b''), (b'8', b'')]),
        ),
    ]
