#!/usr/local/bin/python
# coding: utf-8

from __future__ import unicode_literals
#from sportapp import forms as sport_forms
from django.shortcuts import render
from healthylifeapp import views as general_views
from sportapp import forms as sport_forms
from shop import views as shop_views

# Sport views
def sport(request):
    """
    """
    sport_information = None
    sport_filter_form = getSportFilterForm(request)

    shoppingcart = shop_views.getShoppingCart(request.session)

    return render(request, 'sport.html', {
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'sport_filter_form': getSportFilterForm(request),
        'sport_information': sport_information,
        'shoppingcart': shoppingcart,
    })


def getSportFilterForm(request):
    if request.method == 'POST':
        sport_filter_form = sport_forms.SportFilter(request.POST)
    else:
        sport_filter_form = sport_forms.SportFilter()

    return sport_filter_form


def getExerciseApiInformation(exercise):
    """
    Method that request on exercise api
    """

    url = "https://trackapi.nutritionix.com/v2/natural/exercise"
    """
    Estimate calories burned for various exercises using natural language.  Developer can optionally include user demographics like age, gender, weight to make a more accurate estimate for calories burned.
    https://gist.github.com/mattsilv/d99cd145cc2d44d71fa5d15dd4829e03
    """

    body = {
        'query': health,
    }
    headers = {
        'x-app-id': settings.X_APP_ID,
        'x-app-key': settings.X_APP_KEY,
        #'x-remote-user-id': "7a43c5ba-50e7-44fb-b2b4-bbd1b7d22632",
    }
    response = requests.request("GET", url, params=body, headers=headers)
    content = response.json()

    return content






#
