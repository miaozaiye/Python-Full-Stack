# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-02 13:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0028_auto_20170202_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='choice',
            new_name='voter_choice',
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateField(default=datetime.datetime(2017, 2, 2, 13, 24, 21, 448726)),
        ),
    ]
