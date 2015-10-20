# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20151020_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='addressLogitude',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
