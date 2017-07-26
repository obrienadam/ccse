# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Participant(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)

class Workshop(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    participants = models.ManyToManyField(Participant)
