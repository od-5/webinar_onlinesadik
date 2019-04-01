# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Ticket


class TicketForm(forms.ModelForm):
    terms = forms.BooleanField(required=True)
    code = forms.CharField(required=True)

    class Meta:
        model = Ticket
        fields = ('name', 'phone' , 'mail',)

    def clean_phone(self):
        code = self.data.get('code')
        phone = self.cleaned_data.get('phone')
        return '%s %s' % (code, phone)