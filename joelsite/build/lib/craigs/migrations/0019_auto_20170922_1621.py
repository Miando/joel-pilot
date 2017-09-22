# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('craigs', '0018_auto_20170921_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapedinfo',
            name='job_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='craigs.PersonOptions'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scrapedinfo',
            name='url',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]