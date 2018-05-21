# coding=utf-8
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, CreateView
from django.views.generic.base import ContextMixin
from django.shortcuts import get_object_or_404

from .models import Ticket, Setup


class SetupMixin(ContextMixin):
    """
    Миксин добавляет сео настройки
    """
    def get_context_data(self, **kwargs):
        kwargs = super(SetupMixin, self).get_context_data(**kwargs)
        setup = Setup.objects.first()
        kwargs.update({
            'SETUP': setup
        })
        return kwargs


class LandingView(TemplateView, SetupMixin):
    template_name = 'index.html'


class OkView(TemplateView, SetupMixin):
    template_name = 'ok.html'


class TicketView(CreateView):
    model = Ticket
    fields = ['name', 'phone', 'mail', 'theme',]
    success_url = reverse_lazy('ok')
    template_name = 'index.html'
