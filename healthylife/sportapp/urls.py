#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import url
from django.urls import path, include, re_path
from sportapp import views as sport_views

# Sport URLS's
urlpatterns = [

    url('', sport_views.sport, name='sport'),
    url('ejercicios/', sport_views.sport, name='search_sport'),
]
