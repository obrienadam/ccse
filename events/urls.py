from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^$', view=EventsView.as_view(), name='events'),
    url(r'^(?P<pk>[0-9]+)/$', view=EventView.as_view(), name='event'),
]