# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20160104_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='flag',
            field=models.BooleanField(default=False),
        ),
    ]
