# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_postalcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postalcode',
            name='postalCode',
            field=models.IntegerField(),
        ),
    ]
