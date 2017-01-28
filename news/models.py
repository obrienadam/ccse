from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

    author = models.ForeignKey(User)

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def abstract(self):
        return strip_tags(self.content)[:255]

    def __str__(self):
        return '{}: {}'.format(self.date_added.date(), self.title)
