# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_notificationboard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificationboard',
            old_name='coupon_valid_until_time',
            new_name='notification_valid_until_time',
        ),
    ]
