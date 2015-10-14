# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('amount', models.FloatField(null=True, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('weight', models.FloatField(null=True, blank=True)),
                ('status', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'created'), (b'2', b'wash'), (b'3', b'dry'), (b'4', b'iron'), (b'5', b'complete')])),
                ('created_at_time', models.DateTimeField(auto_now_add=True)),
                ('delivery_id', models.CharField(max_length=200, null=True, blank=True)),
                ('roadrunner_order_id', models.CharField(max_length=200, null=True, blank=True)),
                ('owner', models.ForeignKey(related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
