#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import url
from django.urls import path, include, re_path
from events import views as calendar_views
from events import models as calendar_models

urlpatterns = [

    # Calendar URLS's
    path('<str:username>/<int:year>/<int:month>/', calendar_views.month, name='month_calendar'),
    path('<str:username>/<int:year>/<int:month>/<int:day>/', calendar_views.day, name='day_calendar'),

    # Event Urls
    path('eventos/', calendar_views.list_events, name='list_events'),
    path('eventos/nuevo/', calendar_views.add_event, name='add_event'),
    path('eventos/<str:slug>/', calendar_views.EventUpdateView.as_view(), name='detail_event'),
]
