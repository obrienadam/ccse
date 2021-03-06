# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20170726_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterUniqueTogether(
            name='room',
            unique_together=set([('building', 'number')]),
        ),
    ]
