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
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=10)),
                ('owner', models.OneToOneField(related_name='UserInfo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=255)),
                ('addressLocality', models.CharField(max_length=255, null=True, blank=True)),
                ('addressSubLocality', models.CharField(max_length=100, null=True, blank=True)),
                ('addressLatitude', models.FloatField(null=True, blank=True)),
                ('addressLogitude', models.FloatField(null=True, blank=True)),
                ('created_at_time', models.DateTimeField(auto_now_add=True)),
                ('flag', models.BooleanField(default=0)),
                ('owner', models.ForeignKey(related_name='UserProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
