# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0009_auto_20171014_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='你听说过？', max_length=10, verbose_name='机构标签'),
        ),
    ]
