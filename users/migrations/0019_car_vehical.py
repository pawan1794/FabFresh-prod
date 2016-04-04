# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20160122_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'80')),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('capacity', models.IntegerField()),
                ('mp', models.ForeignKey(to='users.Car')),
            ],
        ),
    ]
