# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-15 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0010_auto_20170822_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='deploymentremake',
            field=models.TextField(blank=True, help_text='\u5907\u6ce8', max_length=1024),
        ),
        migrations.AddField(
            model_name='server',
            name='deploymentversion',
            field=models.CharField(blank=True, help_text='\u7248\u672c\u53f7', max_length=16),
        ),
        migrations.AddField(
            model_name='server',
            name='manage_url',
            field=models.CharField(blank=True, help_text='\u540e\u53f0\u7ba1\u7406\u5730\u5740', max_length=128),
        ),
        migrations.AddField(
            model_name='server',
            name='school_url',
            field=models.CharField(blank=True, help_text='\u5b66\u751f\u767b\u5f55\u5730\u5740', max_length=128),
        ),
        migrations.AddField(
            model_name='server',
            name='special_modify',
            field=models.CharField(blank=True, help_text='\u7279\u6b8a\u4fee\u6539', max_length=128),
        ),
    ]
