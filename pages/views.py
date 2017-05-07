from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from django.utils import timezone

from events.models import Event
from news.models import News
from pages.models import StudentOrganizer

class HomeView(View):
    def get(self, request):
        upcoming_events = Event.objects.filter(date__gte=timezone.now()).order_by('date', 'start_time')[:3]
        past_events = Event.objects.filter(date__lt=timezone.now()).order_by('-date', '-start_time')[:3]
        news = News.objects.all()[:6]

        return render(request, 'pages/home.html', {
            'upcoming_events': upcoming_events,
            'past_events': past_events,
            'news': news
        })

class OverviewView(TemplateView):
    template_name = 'pages/overview.html'

class PeopleView(View):
    def get(self, request):
        return render(request, 'pages/people.html', {'students': StudentOrganizer.objects.all()})

class ComputingFacilities(TemplateView):
    template_name = 'pages/computing_facilities.html'