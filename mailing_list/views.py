# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView, DetailView
from django.core.urlresolvers import reverse
from django.core import mail
from django.db import models
from django.utils import timezone

from .forms import SubscribtionForm
from .models import Subscriber


# Create your views here.
class SubscribtionFormView(FormView):
    form_class = SubscribtionForm
    template_name = 'mailing_list/subscribe.html'

    def get_success_url(self):
        return reverse('mailing-list:subscription-success')

    def form_valid(self, form):
        new_subscriber = form.save(commit=False)
        email = new_subscriber.email
        token = new_subscriber.confirmation_token
        conf_url = '{}?token={}'.format(self.request.build_absolute_uri(reverse('mailing-list:confirm-subscription')), token)

        message = """Thank you for subscribing to the CCSE mailing list! We hope to see you at an event in the near future.
        
To confirm your e-mail address, please click on the following link:

{}

If you did not sign up for the CCSE mailing list, please disregard this e-mail.

Thank you,

CCSE Organizing Committee""".format(conf_url)

        with mail.get_connection() as connection:
            mail.EmailMessage(subject='CCSE Mailing List: Confirm E-mail',
                              to=[email],
                              connection=connection,
                              body=message).send()

        new_subscriber.save()

        return HttpResponseRedirect('{}?email={}'.format(reverse('mailing-list:subscription-success'), new_subscriber.email))

class SubscriptionSuccessView(TemplateView):
    template_name = 'mailing_list/subscription_success.html'

    def get_context_data(self, **kwargs):
        kwargs['email'] = self.request.GET.get('email')
        return super(SubscriptionSuccessView, self).get_context_data(**kwargs)

class SubscribtionConfirmationView(TemplateView):
    template_name = 'mailing_list/confim_subscription.html'

    def get_context_data(self, **kwargs):
        token = self.request.GET.get('token')

        try:
            subscriber = Subscriber.objects.get(confirmation_token=token)

            if not subscriber.confirmed:
                subscriber.confirmed = True
                subscriber.confirmed_on = timezone.now()
                subscriber.save()

            kwargs['subscriber_confirmed'] = True
        except models.ObjectDoesNotExist:
            kwargs['subscriber_confirmed'] = False

        return super(SubscribtionConfirmationView, self).get_context_data(**kwargs)

class UnsubscribeView(TemplateView):
    template_name = 'mailing_list/unsubscribe.html'

    def get_context_data(self, **kwargs):
        try:
            subscriber = Subscriber.objects.get(confirmation_token=self.request.GET.get('token'))
            subscriber.delete()
            kwargs['success'] = True
        except models.ObjectDoesNotExist:
            kwargs['success'] = False

        return super(UnsubscribeView, self).get_context_data(**kwargs)
