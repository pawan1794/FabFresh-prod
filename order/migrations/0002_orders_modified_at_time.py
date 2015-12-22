# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='modified_at_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
