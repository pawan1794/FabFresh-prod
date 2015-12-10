# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20151210_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postalcode',
            name='id',
        ),
        migrations.AddField(
            model_name='postalcode',
            name='Locality',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='postalcode',
            name='postalCode',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
