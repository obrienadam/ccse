# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presenter',
            name='affiliation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
