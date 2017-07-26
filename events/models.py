from __future__ import unicode_literals

from django.db import models
from locations.models import Room

class Event(models.Model):
    SEMINAR = 0
    MEETING = 1
    LECTURE = 2

    EVENT_TYPES = (
        (0, 'Seminar'),
        (1, 'Meeting'),
        (2, 'Lecture'),
    )

    event_type = models.SmallIntegerField(choices=EVENT_TYPES, default=SEMINAR)
    title = models.CharField(max_length=128)
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.ForeignKey(Room, blank=True, null=True)

    visible = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-start_time', '-end_time']

    def get_start(self):
        return self.start_time.strftime('%I:%M %p') if self.start_time else ''

    def get_end(self):
        return self.end_time.strftime('%I:%M %p') if self.end_time else ''

    def time_slot(self):
        return '{} - {}'.format(self.get_start(), self.get_end()) if self.start_time else 'TBD'

    def __str__(self):
        return '{}: {}'.format(self.get_event_type_display(), self.title)

class Presentation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    abstract = models.TextField(blank=True, null=True)
    pdf_abstract = models.FileField(blank=True, null=True)

    def __str__(self):
        return 'Presentation: {}'.format(self.title)

    def get_presenters(self):
        presenters = ''
        for presenter in self.presenter_set.all():
            presenters += str(presenter) + ', '

        return presenters[:-2]

class University(models.Model):
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return '{}, {} {}'.format(self.name, self.city, self.country)

class Department(models.Model):
    university = models.ForeignKey(University)
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Presenter(models.Model):
    NONE = 0
    DOCTOR = 1
    PROFESSOR = 2

    HONORARY_TYPES = (
        (0, ''),
        (1, 'Dr.'),
        (2, 'Prof.'),
    )

    presentation = models.ManyToManyField(Presentation, blank=True)
    affiliation = models.ForeignKey(Department, on_delete=None, blank=True, null=True)

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    honorary = models.PositiveSmallIntegerField(choices=HONORARY_TYPES, default=NONE)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return '{} {} {}'.format(self.get_honorary_display(), self.first_name, self.last_name).strip().title()