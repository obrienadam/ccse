from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^$', view=EventsView.as_view(), name='events'),
    url(r'^(?P<slug>[-\w\d]+)-(?P<pk>\d+)/$', view=EventView.as_view(), name='event'),
    url(r'^cses2019/$', view=EventsView.as_view(), name='cses2019'),
    url(r'^cses2019/(?P<slug>[-\w]+)/$', view=EventsView.as_view(), name='cses2019')
]