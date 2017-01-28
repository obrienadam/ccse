from django.conf.urls import url

from views import *

urlpatterns = [
    url('^$', view=GroupListView.as_view(), name='groups'),
]