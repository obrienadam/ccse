# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-26 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_event_ics_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]