# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-14 09:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 14, 15, 23, 49, 659000)),
        ),
    ]
