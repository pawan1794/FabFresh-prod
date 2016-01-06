# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_auto_20160106_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='type_price',
            new_name='type_price_iron',
        ),
        migrations.AddField(
            model_name='type',
            name='type_price_wash',
            field=models.FloatField(default=0.0, max_length=100000, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='type',
            name='type_price_wash_and_iron',
            field=models.FloatField(default=0.0, max_length=100000, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
