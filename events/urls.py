from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^$', view=EventsView.as_view(), name='events'),
    url(r'^(?P<slug>[-\w\d]+)-(?P<pk>\d+)/$', view=EventView.as_view(), name='event')
]