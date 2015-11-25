# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151124_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='userProfile',
            field=models.ForeignKey(related_name='address', to=settings.AUTH_USER_MODEL),
        ),
    ]
