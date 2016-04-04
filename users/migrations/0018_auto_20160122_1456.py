# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20160122_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allinone',
            name='abc',
            field=models.IntegerField(),
        ),
    ]
