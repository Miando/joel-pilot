# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craigs', '0003_auto_20170901_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryoptions',
            name='city',
        ),
        migrations.AlterField(
            model_name='additionaloptions',
            name='option',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='additionaloptions',
            name='option_for_frontend',
            field=models.CharField(default='all', max_length=250),
        ),
        migrations.AlterField(
            model_name='subcategoryoptions',
            name='subcategory',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='subcategoryoptions',
            name='subcategory_for_frontend',
            field=models.CharField(default='all', max_length=250),
        ),
    ]
