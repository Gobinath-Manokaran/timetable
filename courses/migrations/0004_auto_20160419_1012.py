# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 10:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20160419_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='day',
        ),
        migrations.AddField(
            model_name='classes',
            name='days',
            field=models.CharField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], default=datetime.datetime(2016, 4, 19, 10, 12, 20, 727717, tzinfo=utc), max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classes',
            name='end_date',
            field=models.TimeField(verbose_name='Class End time'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='start_date',
            field=models.TimeField(verbose_name='Class start time'),
        ),
    ]