# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0002_auto_20170615_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='operatingsystem',
            name='domain_name',
            field=models.CharField(blank=True, help_text='\u57df\u540d', max_length=64),
        ),
    ]
