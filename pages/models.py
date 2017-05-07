from __future__ import unicode_literals

from django.db import models

class StudentOrganizer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(blank=True, null=True, upload_to='student_organizers')
    bio = models.TextField(max_length=500)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name.title()

