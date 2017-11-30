from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^subscribe/$', view=SubscribtionFormView.as_view(), name='subscribtion-form'),
    url(r'^subscription-success/$', view=SubscriptionSuccessView.as_view(), name='subscription-success'),
    url(r'^confirm-subscribtion/$', view=SubscribtionConfirmationView.as_view(), name='confirm-subscription'),
    url(r'^unsubscribe/$', view=UnsubscribeView.as_view(), name='unsubscribe')
]