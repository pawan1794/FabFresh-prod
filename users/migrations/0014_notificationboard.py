# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_androidappversion'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationBoard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('coupon_valid_until_time', models.DateTimeField()),
            ],
        ),
    ]
