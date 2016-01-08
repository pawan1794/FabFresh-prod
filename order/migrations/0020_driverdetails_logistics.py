# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_auto_20160106_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverdetails',
            name='logistics',
            field=models.CharField(default=1, max_length=1, choices=[(b'1', b'roadrunner'), (b'2', b'shadowfax')]),
        ),
    ]
