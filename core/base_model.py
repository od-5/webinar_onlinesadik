# coding=utf-8
from django.db import models
from core.models import User

__author__ = 'alexey'


class Common(models.Model):
    title = models.CharField(max_length=256, verbose_name=u'Заголовок')
    meta_key = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'META ключевые слова')
    meta_desc = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'META описание')

    class Meta:
        abstract = True
        ordering = ['-created', ]


class CommonPage(Common):
    meta_title = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'META заголовок')
    created = models.DateField(verbose_name=u'Дата создания', auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title
