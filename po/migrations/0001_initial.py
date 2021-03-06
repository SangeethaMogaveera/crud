# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-20 07:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendors', '0005_auto_20170820_0753'),
        ('material', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Po',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expected_date', models.DateField(blank=True, null=True, verbose_name=b'expected_date')),
                ('comment', models.TextField(max_length=800)),
                ('status', models.CharField(choices=[(b'or', b'Ordered'), (b'in', b'In Progress'), (b'par', b'Partial Delivered'), (b'del', b'Delivered')], default=True, max_length=300)),
                ('material', models.ManyToManyField(to='material.Material')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.Vendor')),
            ],
        ),
    ]
