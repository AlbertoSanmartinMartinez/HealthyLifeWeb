#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from healthylifeapp import views as general_views
from shop import views as shop_views

# Create your views here.
def health(request):

    shoppingcart = shop_views.getShoppingCart(request.session)

    return render(request, 'health.html', {
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'shoppingcart': shoppingcart,
    })
