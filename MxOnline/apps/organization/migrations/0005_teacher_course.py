# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='course',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='讲授课程'),
        ),
    ]
