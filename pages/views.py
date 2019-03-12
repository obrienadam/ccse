from django.conf import settings
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.utils import timezone

from events.models import Event
from pages.models import StudentOrganizer

class HomeView(View):
    def get(self, request):
        upcoming_events = Event.objects.filter(date__gte=timezone.now(), visible=True).order_by('date', 'start_time')[:3]
        past_events = Event.objects.filter(date__lt=timezone.now(), visible=True).order_by('-date', '-start_time')[:3]

        return render(request, 'pages/home.html', {
            'upcoming_events': upcoming_events,
            'past_events': past_events,
            'next_event': upcoming_events[0] if upcoming_events else None,
            'last_event': past_events[0] if past_events else None,
            'twitter_heading': settings.TWITTER_HEADING,
            'twitter_url': settings.TWITTER_URL,
            'twitter_data_tweet_limit': settings.TWITTER_DATA_TWEET_LIMIT
        })

class OverviewView(TemplateView):
    template_name = 'pages/overview.html'

class Cses2019View(TemplateView):
    template_name = 'pages/cses2019.html'

class PeopleView(View):
    def get(self, request):
        return render(request, 'pages/people.html', {'students': StudentOrganizer.objects.all()})

class ComputingFacilities(TemplateView):
    template_name = 'pages/computing_facilities.html'