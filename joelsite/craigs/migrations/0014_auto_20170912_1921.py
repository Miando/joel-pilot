# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craigs', '0013_auto_20170912_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategoryoptions',
            name='category',
            field=models.CharField(default='', max_length=250),
        ),
    ]
