from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^$', view=NewsView.as_view(), name='news'),
    url(r'^(?P<pk>[0-9]+)/$', view=ArticleView.as_view(), name='article'),
]