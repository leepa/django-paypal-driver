from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^base/', include("testapp.base.urls")),
    url(r'^$', "django.views.generic.simple.redirect_to", {"url": "/base/setcheckout/"})                       
                       
)
