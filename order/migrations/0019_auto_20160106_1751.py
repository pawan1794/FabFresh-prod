# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0018_auto_20160106_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='type_name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
