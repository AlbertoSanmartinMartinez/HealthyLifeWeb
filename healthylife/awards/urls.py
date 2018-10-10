#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import url
from django.urls import path, include
from awards import views as awards_views

urlpatterns = [

    # Awards URLS's
    path('', awards_views.awards, name='awards'),
    path('', awards_views.awards, name='search_awards'),

    path('<str:username>/conseguidos/', awards_views.awards_profile, name='awards_profile'),

    path('<str:award_slug>/', awards_views.award_detail, name='award_detail'),

    # Coupon Urls
    path('cupon/', awards_views.coupon, name='coupon'),
]
