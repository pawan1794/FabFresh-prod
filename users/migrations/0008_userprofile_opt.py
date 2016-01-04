# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20151210_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='opt',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
