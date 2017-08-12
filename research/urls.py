from django.conf.urls import url

import views

urlpatterns = [
    url(r'^groups/$', view=views.GroupListView.as_view(), name='groups'),
    url(r'^groups/(?P<slug>[-\w]+)/$', view=views.GroupDetailView.as_view(), name='group'),
    url(r'^fields/$', view=views.FieldListView.as_view(), name='fields'),
    url(r'^fields/(?P<slug>[-\w]+)/$', view=views.FieldDetailView.as_view(), name='field')
]
