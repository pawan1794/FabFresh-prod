# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orders_modified_at_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusTimeStamp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'1', max_length=1, choices=[(b'0', b'cancelled'), (b'1', b'created'), (b'2', b'pickup'), (b'3', b'receivedAtCenter'), (b'4', b'tagging'), (b'5', b'preCheck'), (b'6', b'wash'), (b'7', b'dry'), (b'8', b'iron'), (b'9', b'package'), (b'10', b'shipped'), (b'11', b'drop'), (b'12', b'completed')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'0', b'cancelled'), (b'1', b'created'), (b'2', b'pickup'), (b'3', b'receivedAtCenter'), (b'4', b'tagging'), (b'5', b'preCheck'), (b'6', b'wash'), (b'7', b'dry'), (b'8', b'iron'), (b'9', b'package'), (b'10', b'shipped'), (b'11', b'drop'), (b'12', b'completed')]),
        ),
        migrations.AddField(
            model_name='statustimestamp',
            name='orders',
            field=models.ForeignKey(related_name='orders', to='order.orders'),
        ),
    ]
