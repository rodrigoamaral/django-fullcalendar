from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'demo.views.index', name='index'),
    url(r'^all_events/', 'demo.views.all_events', name='all_events'),
    url(r'^admin/', include(admin.site.urls)),
)
