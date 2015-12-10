# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20151210_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='postalCode',
            field=models.IntegerField(),
        ),
    ]
