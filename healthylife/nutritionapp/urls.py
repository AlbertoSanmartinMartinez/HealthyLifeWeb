#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import url
from django.urls import path, include, re_path
from nutritionapp import views as nutrition_views

# Nutrition URLS's
urlpatterns = [

    path('', nutrition_views.nutrition, name='nutrition'),
    path('informacion_nutricional/', nutrition_views.nutrition, name='search_food'),
]
