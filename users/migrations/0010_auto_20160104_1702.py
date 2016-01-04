# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20160104_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='opt',
            new_name='otp',
        ),
    ]
