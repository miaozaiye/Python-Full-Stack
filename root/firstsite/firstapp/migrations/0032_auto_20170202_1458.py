# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-02 14:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0031_auto_20170202_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateField(default=datetime.datetime(2017, 2, 2, 14, 58, 24, 764371)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(blank=True, choices=[('dxs', '大学生'), ('lnr', '老年人'), ('信用卡', '信用卡'), ('扫二维码', '扫二维码'), ('短信', '短信'), ('邮件', '邮件'), ('奖学金', '奖学金')], max_length=5, null=True),
        ),
    ]
