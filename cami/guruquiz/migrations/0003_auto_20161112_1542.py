# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guruquiz', '0002_auto_20161112_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='video',
            name='transcript',
            field=models.TextField(blank=True),
        ),
    ]
