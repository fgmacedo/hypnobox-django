# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-21 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hypnobox', '0003_auto_20160913_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='description'),
        ),
    ]
