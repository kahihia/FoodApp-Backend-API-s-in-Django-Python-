# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-16 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUsers',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('mobile_no', models.IntegerField(max_length=12)),
            ],
        ),
    ]
