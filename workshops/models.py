# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Workshop(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

class ResourceFile(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    file = models.FileField(upload_to='workshops')


