# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20151124_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.RemoveField(
            model_name='locality',
            name='city',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Locality',
        ),
    ]
