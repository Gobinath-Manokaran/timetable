# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20160420_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='day',
            field=models.CharField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (0, 'Sunday')], max_length=20),
        ),
    ]
