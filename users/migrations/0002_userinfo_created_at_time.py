# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='created_at_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 15, 8, 17, 25, 31670, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
