from django.contrib import admin

from models import Event, Presentation, Presenter

class PresentationInline(admin.StackedInline):
    model = Presentation
    extra = 3

class PresenterInline(admin.StackedInline):
    model = Presenter
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [PresentationInline]
    list_display = ('title', 'date', 'get_start', 'get_end', 'location')

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    inlines = [PresenterInline]
    list_display = ('title', 'get_presenters')