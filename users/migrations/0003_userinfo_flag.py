# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userinfo_created_at_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='flag',
            field=models.BooleanField(default=0),
        ),
    ]
