# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-20 07:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('consultant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=600)),
                ('site_address', models.CharField(max_length=100)),
                ('construction_place', models.CharField(max_length=100)),
                ('survey_no', models.CharField(max_length=100)),
                ('enabled', models.BooleanField(default=True)),
                ('state', models.BooleanField(choices=[(False, 'Inactive'), (True, 'Active')], default=True, max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime(2017, 8, 20, 7, 52, 42, 60021))),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultant.Consultant')),
            ],
        ),
    ]
