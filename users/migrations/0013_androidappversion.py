# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_wallet'),
    ]

    operations = [
        migrations.CreateModel(
            name='AndroidAppVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('versionNumber', models.FloatField()),
            ],
        ),
    ]
