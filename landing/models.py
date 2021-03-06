from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from core.base_model import Common
from core.models import User


class Setup(Common):
    title = models.CharField(verbose_name=u'Заголовок <TITLE>...</TITLE>', max_length=256, blank=True)
    phone = models.CharField(verbose_name=u'Телефон', max_length=256, blank=True)
    email = models.EmailField(verbose_name=u'e-mail для приёма заявок', blank=True)
    meta_key = models.TextField(verbose_name=u'Ключевые слова META_KEYWORDS', blank=True)
    meta_desc = models.TextField(verbose_name=u'Описание META_DESCRIPTION', blank=True)
    top_js = models.TextField(verbose_name=u'Скрипты в <HEAD>..</HEAD>', blank=True)
    bottom_js = models.TextField(verbose_name=u'Скрипты перед закрывающим </BODY>', blank=True)
    robots_txt = models.TextField(verbose_name=u'ROBOTS.TXT', blank=True, null=True)
    sitemap = models.TextField(verbose_name=u'sitemap.xml', blank=True, null=True)
    insta_link = models.CharField(verbose_name=u'Ссылка на инстаграм', max_length=256, blank=True)
    vk_link = models.CharField(verbose_name=u'Ссылка на Вконтакте', max_length=256, blank=True)
    youtube_link = models.CharField(verbose_name=u'Ссылка на канал youtube', max_length=256, blank=True)

    class Meta:
        verbose_name = u'Настройки сайта'
        verbose_name_plural = u'Настройки сайта'
        app_label = 'landing'

    def __str__(self):
        if self.title:
            return self.title
        else:
            return u'Настройки'

    @property
    def phone_format(self):
        if self.phone:
            formatted_phone = ''.join([i for i in self.phone if i.isdigit()])
        else:
            formatted_phone = None
        return formatted_phone


class Country(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=100)
    code = models.CharField(verbose_name=u'Код страны', max_length=5, default='+7')
    phone_format = models.CharField(verbose_name=u'Маска номера телефона', max_length=16,
                                    default=u'(999) 999-99-99')

    class Meta:
        ordering = ['id']
        verbose_name = u'Страна'
        verbose_name_plural = u'Страны'

    def __str__(self):
        return self.name

    @property
    def phone_mask(self):
        mask = []
        for i in self.phone_format:
            if i.isdigit():
                mask.append('_')
            else:
                mask.append(i)
        return ''.join(mask)

    @property
    def phone_format_d(self):
        return self.phone_format.replace('9', 'd')



class Ticket(models.Model):

    name = models.CharField(verbose_name=u'Имя', max_length=256)
    phone = models.CharField(verbose_name=u'Телефон', max_length=20)
    mail = models.EmailField(verbose_name=u'e-mail', max_length=100, blank=True, null=True)
    theme = models.CharField(verbose_name=u'Тема', max_length=256, blank=True, null=True)
    created = models.DateField(verbose_name=u'Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'
        app_label = 'landing'
        ordering = ['-created']

    def __str__(self):
        return self.name

    def send_admin_mail(self):
        setup = Setup.objects.all().first()
        if setup and setup.email:
            email = setup.email
            mail_theme_msg = u'webinar.onlinesadik.com - %s' % self.theme
            message = u'Тема: %s\nИмя: %s\nТелефон: %s\nE-mail: %s\n' % \
                      (self.theme, self.name, self.phone, self.mail)
            try:
                send_mail(
                    mail_theme_msg,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email, ]
                )
            except:
                pass
        return False


@receiver(post_save, sender=Ticket)
def create_mail(sender, created, **kwargs):
    ticket = kwargs['instance']
    if created:
        ticket.send_admin_mail()
