from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^$', view=HomeView.as_view(), name='home'),
    url(r'^about/overview/$', view=OverviewView.as_view(), name='overview'),
    url(r'^about/people/$', view=PeopleView.as_view(), name='people'),
    url(r'^events/cses2019/$', view=Cses2019View.as_view(), name='cses2019'),
    url(r'^computing/facilities/$', view=ComputingFacilities.as_view(), name='computing-facilities'),
]