# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20151224_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(default=b'1', max_length=2, choices=[(b'0', b'cancelled'), (b'1', b'created'), (b'2', b'pickup'), (b'3', b'receivedAtCenter'), (b'4', b'precheck'), (b'5', b'tagging'), (b'6', b'wash'), (b'7', b'dry'), (b'8', b'iron'), (b'9', b'package'), (b'10', b'shipped'), (b'11', b'drop'), (b'12', b'completed')]),
        ),
    ]
