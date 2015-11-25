# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=255)),
                ('addressSubLocality', models.CharField(max_length=100, null=True, blank=True)),
                ('addressLatitude', models.FloatField(null=True, blank=True)),
                ('addressLogitude', models.FloatField(null=True, blank=True)),
                ('created_at_time', models.DateTimeField(auto_now_add=True)),
                ('flag', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('locality_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(related_name='locality', to='users.City')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='locality',
            field=models.ForeignKey(to='users.Locality'),
        ),
        migrations.AddField(
            model_name='address',
            name='userProfile',
            field=models.ForeignKey(related_name='address', to='users.UserProfile'),
        ),
    ]
