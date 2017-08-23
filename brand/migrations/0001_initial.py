# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-20 07:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subcategory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sub_cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subcategory.Subcategory')),
            ],
        ),
    ]
