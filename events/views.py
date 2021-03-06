from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.utils import timezone
from django.conf import settings

from models import Event

class EventsView(View):
    def get(self, request):
        upcoming_events = Event.objects.filter(date__gte=timezone.now().date(), visible=True).order_by('date', 'start_time')
        past_events = Event.objects.filter(date__lt=timezone.now().date(), visible=True).order_by('-date', '-start_time')

        return render(request, 'events/events.html', {
            'upcoming_events': upcoming_events,
            'past_events': past_events,
        })

class EventView(View):
    def get(self, request, slug, pk):
        event = get_object_or_404(Event, pk=pk, visible=True)
        return render(request,
                      'events/event.html',
                      {
                          'event': event,
                          'room': event.location,
                          'google_api_key': settings.GOOGLE_API_KEY
                      })