#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import url
from django.urls import path, include, re_path
from healthapp import views as health_views

# Health URLS's
urlpatterns = [

    path('', health_views.health, name='health'),

]
