# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_type_type_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='type_price',
            field=models.FloatField(default=0.0, max_length=100000, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
