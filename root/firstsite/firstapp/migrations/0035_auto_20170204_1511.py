# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-04 15:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0034_auto_20170203_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateField(default=datetime.datetime(2017, 2, 4, 15, 11, 41, 570762)),
        ),
    ]
