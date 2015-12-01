# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_userinfo_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(default=7204680605, max_length=10),
            preserve_default=False,
        ),
    ]
