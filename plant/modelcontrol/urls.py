# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from modelcontrol import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<plant_id>\d+)/update/$', views.update, name='update'),
)