# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-16 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appusers',
            name='mobile_no',
            field=models.CharField(max_length=12),
        ),
    ]
