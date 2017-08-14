from __future__ import unicode_literals

from django.db import models
from django.utils import text

import markdown

class Field(models.Model):
    slug = models.SlugField(max_length=128, primary_key=True, blank=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def render_description_html(self):
        return markdown.markdown(self.description)

    def save(self, **kwargs):
        self.slug = text.slugify(self.name)
        super(Field, self).save(**kwargs)

class Group(models.Model):
    slug = models.SlugField(max_length=128, primary_key=True, blank=True)
    name = models.CharField(max_length=128)
    site = models.URLField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    description = models.TextField()
    fields = models.ManyToManyField(Field, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = text.slugify(self.name)
        super(Group, self).save(**kwargs)

    def render_abstract(self):
        if not self.abstract:
            self.abstract = self.description

        if len(self.abstract) <= 500:
            return self.abstract
        else:
            return self.abstract[:497] + '...'

    def render_html(self):
        imgs = '\n'
        for img in self.image_set.all():
            imgs += '\n[{}]: {}'.format(img.tag, img.img.url)

        return markdown.markdown(self.description + imgs, extensions=['markdown.extensions.attr_list'])

def image_file_path(instance, filename):
    return 'groups/{}/{}'.format(instance.group.slug, filename)

class Image(models.Model):
    group = models.ForeignKey(Group)
    tag = models.CharField(max_length=32)
    img = models.ImageField(upload_to=image_file_path, max_length=128)

    class Meta:
        unique_together = (('group', 'tag'),)

    def markdown_tag(self):
        return '![alt text][{}]'.format(self.tag)




