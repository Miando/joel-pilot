# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('craigs', '0016_auto_20170915_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personoptions',
            name='keyword',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='personoptions',
            name='time_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
