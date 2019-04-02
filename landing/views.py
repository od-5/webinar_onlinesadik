# coding=utf-8
import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.views.generic.base import ContextMixin

from landing.forms import TicketForm
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
    form_class = TicketForm
    success_url = reverse_lazy('index')
    template_name = 'index.html'


@login_required
def ticket_csv(request):
    qs = Ticket.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    for i in qs:
        writer.writerow([i.name.encode('utf8'), i.phone.encode('utf8'), i.mail.encode('utf8')])
    return response
