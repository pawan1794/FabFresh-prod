# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_userprofile_opt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='opt',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='opt',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
