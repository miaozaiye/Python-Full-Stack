# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-05 06:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0036_auto_20170204_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateField(default=datetime.datetime(2017, 2, 5, 6, 2, 2, 719964)),
        ),
    ]
