# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20160115_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='androidappversion',
            name='serverShutdown',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='androidappversion',
            name='serverShutdownReason',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
