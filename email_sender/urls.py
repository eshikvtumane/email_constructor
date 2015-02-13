from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()




urlpatterns = patterns('',
    url(r'^(?P<email_id>[0-9]+)/$', 'email_sender.views.email_send'),
)