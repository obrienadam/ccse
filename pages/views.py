from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.utils import timezone

from events.models import Event
from news.models import News

class HomeView(View):
    def get(self, request):
        events = Event.objects.filter(date__gte=timezone.now()).order_by('date', 'start_time')
        news = News.objects.all()[:6]

        return render(request, 'pages/home.html', {
            'events': events,
            'news': news
        })

class OverviewView(TemplateView):
    template_name = 'pages/overview.html'

class PeopleView(TemplateView):
    template_name = 'pages/people.html'

class ComputingFacilities(TemplateView):
    template_name = 'pages/computing_facilities.html'