# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0026_auto_20160115_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothsplitprice',
            name='invoiceid',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
