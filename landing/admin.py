# coding=utf-8
from django.contrib import admin
from django.template.loader import render_to_string
from django.conf.urls import url

from .models import Ticket, Setup


class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'mail', 'theme')
    list_filter = ['mail', 'created', 'theme']
    search_fields = ['mail', ]
    date_hierarchy = 'created'


class SetupAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if Setup.objects.exists():
            return False
        else:
            return True


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Setup, SetupAdmin)
