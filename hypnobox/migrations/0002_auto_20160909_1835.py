# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-09 21:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hypnobox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='phone_number',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('^[\\d\\-]+$', message='Only numbers.')], verbose_name='phone number'),
        ),
    ]