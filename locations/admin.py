# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Location, Building, Room

class BuildingInline(admin.StackedInline):
    model = Building

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = (BuildingInline, )

@admin.register(Room)
class RooomAdmin(admin.ModelAdmin):
    pass
