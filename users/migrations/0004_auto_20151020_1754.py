# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userinfo_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='addressLatitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='addressLocality',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='addressSubLocality',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
