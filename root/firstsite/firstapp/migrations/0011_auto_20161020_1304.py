# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 13:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_auto_20161020_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2016, 10, 20, 13, 4, 45, 958491)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateField(default=datetime.datetime(2016, 10, 20, 13, 4, 45, 959831)),
        ),
    ]
