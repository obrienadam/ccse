# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Location(models.Model):
    PROVINCES = (
        ('AB', 'Alberta'),
        ('BC', 'British Columbia'),
        ('MB', 'Manitoba'),
        ('NB', 'New Brunswick'),
        ('NL', 'Newfoundland'),
        ('NT', 'Northwest Territories'),
        ('NS', 'Nova Scotia'),
        ('NU', 'Nunavut'),
        ('ON', 'Ontario'),
        ('PE', 'Prince Edward Island'),
        ('QC', 'Quebec'),
        ('SK', 'Saskatchewan'),
        ('YT', 'Yukon'),
    )

    city = models.CharField(max_length=128, default='Toronto')
    province = models.CharField(max_length=2, choices=PROVINCES, default='ON')
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True, null=True)
    postal_code = models.CharField(max_length=6)
    place_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        if self.building:
            return str(self.building)
        else:
            return '{}, {}, {} {}'.format(self.address_1, self.city, self.province, self.postal_code)

class Building(models.Model):
    location = models.OneToOneField(Location)
    name = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.code)

    def save(self, **kwargs):
        super(Building, self).save(**kwargs)
        Room(building=self, number='TBD').save()

    def address(self):
        loc = self.location

        if loc.address_2:
            return '{}, {}, {}, {}, {} {}'.format(self.name, loc.address_1, loc.address_2, loc.city, loc.province, loc.postal_code)
        else:
            return '{}, {}, {}, {} {}'.format(self.name, loc.address_1, loc.city, loc.province, loc.postal_code)

class Room(models.Model):
    building = models.ForeignKey(Building)
    number = models.CharField(max_length=16)
    max_occupancy = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        unique_together = (('building', 'number'),)

    def __str__(self):
        return '{} {}'.format(self.building.code, self.number)
