# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20160419_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='classes',
        ),
        migrations.AddField(
            model_name='courses',
            name='classes',
            field=models.ManyToManyField(to='courses.Classes'),
        ),
    ]