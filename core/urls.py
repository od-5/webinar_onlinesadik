# coding=utf-8
from django.conf.urls import url

from core.views import get_robots_txt, get_sitemap_xml

__author__ = 'alexy'


urlpatterns = [
    url(r'^robots\.txt', get_robots_txt, name='robots'),
    url(r'^sitemap\.xml', get_sitemap_xml, name='sitemap'),
]
