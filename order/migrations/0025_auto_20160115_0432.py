# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0024_clothsplitprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothsplitprice',
            name='typeName',
            field=models.CharField(max_length=100),
        ),
    ]
