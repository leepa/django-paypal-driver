from django.conf.urls.defaults import *

from django.contrib import admin
from django.contrib.sites.models import Site

admin.autodiscover()

site = Site.objects.get_current()
urlpatterns = patterns('',
    url(r'^setcheckout/$', 'paypal.views.setcheckout',
        {'return_url': site.domain + "/base/docheckout/",
         'cancel_url': site.domain + '/base/cancel/',
         'error_url': site.domain + '/base/error/',
         }, name = "paypal-setcheckout"),
                       
    url(r'^docheckout/$', 'paypal.views.docheckout',
        {'success_url': site.domain + "/base/success/",
         'error_url': site.domain + '/base/error/',
         }, name = "paypal-docheckout"),                       

    url(r'^dorefund/$', 'paypal.views.dorefund',
        {'success_url': site.domain + "/base/success/",
         'error_url': site.domain + '/base/error/',
         }, name = "paypal-dorefund"),
                       
    url(r'^cancel/$', 'testapp.base.views.cancel_page', name = "base-cancel"),
    url(r'^success/$', 'testapp.base.views.success_page', name = "base-success"),                       
    url(r'^error/$', 'testapp.base.views.error_page', name = "base-error"),
                       
)
