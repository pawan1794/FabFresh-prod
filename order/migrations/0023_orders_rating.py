# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0022_auto_20160112_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='rating',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
