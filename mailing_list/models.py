# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models

# Create your models here.
class Subscriber(models.Model):
    confirmation_token = models.UUIDField(default=uuid.uuid4, primary_key=True)
    first_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='First Name')
    last_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='Last Name')
    email = models.EmailField(max_length=256, blank=False, null=False, verbose_name='E-mail', unique=True)
    confirmed = models.BooleanField(default=False)
    subscribed_on = models.DateTimeField(auto_now_add=True)
    confirmed_on = models.DateTimeField(blank=True, null=True)

class Letter(models.Model):
    subject = models.CharField(max_length=128)
    content = models.TextField()
    draft = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    saved_on = models.DateTimeField(auto_now=True)
    sent_on = models.DateTimeField(blank=True, null=True)