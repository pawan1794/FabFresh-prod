# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20151124_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='userProfile',
            new_name='user',
        ),
    ]
