# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-02 02:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0038_auto_20170302_0219'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Idontlike',
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateField(default=datetime.datetime(2017, 3, 2, 2, 19, 51, 149946)),
        ),
    ]