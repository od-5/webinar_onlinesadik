"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from landing.views import LandingView, OkView, TicketView, ticket_csv, get_country_format

urlpatterns = [
    url(r'^$', LandingView.as_view(), name='index'),
    url(r'^ticket/$', TicketView.as_view(), name='ticket'),
    url(r'^ticket/csv/$', ticket_csv, name='ticket-csv'),
    url(r'^ok/$', OkView.as_view(), name='ok'),
    url(r'^admin/', admin.site.urls),
    url(r'^ajax/country/format/$', get_country_format, name='country-format'),
    url(r'', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
