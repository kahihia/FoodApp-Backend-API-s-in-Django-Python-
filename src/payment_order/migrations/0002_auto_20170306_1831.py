# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-06 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_order',
            name='payment_order_receipt_no',
            field=models.CharField(max_length=30),
        ),
    ]
