from django.contrib import admin

from models import Event, Presentation, University, Department, Presenter

class PresentationInline(admin.StackedInline):
    model = Presentation
    extra = 3

class DepartmentInline(admin.StackedInline):
    model = Department
    extra = 3

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [PresentationInline]
    list_display = ('title', 'date', 'get_start', 'get_end', 'location')

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_presenters')

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    inlines = [DepartmentInline]
    list_display = ('name', 'city', 'country')

@admin.register(Presenter)
class PresenterAdmin(admin.ModelAdmin):
    pass