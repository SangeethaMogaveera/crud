# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-14 10:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_auto_20160714_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='validityoflicences',
            name='mst_no',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 14, 15, 36, 42, 370000)),
        ),
    ]
