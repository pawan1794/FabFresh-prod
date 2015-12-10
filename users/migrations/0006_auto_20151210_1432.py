# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20151210_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='postalCode',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='postalcode',
            field=models.ForeignKey(related_name='postalcode', default=560034, to='users.PostalCode'),
            preserve_default=False,
        ),
    ]
