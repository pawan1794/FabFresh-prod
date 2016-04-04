# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20160115_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllInOne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abc', models.IntegerField(default=56)),
            ],
        ),
        migrations.AlterField(
            model_name='wallet',
            name='wallet',
            field=models.FloatField(default=0, max_length=1000000, verbose_name=b'money'),
        ),
    ]
