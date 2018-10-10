#!/usr/local/bin/python
# coding: utf-8

from __future__ import unicode_literals
from nutritionapp import forms as nutrition_forms
from django.shortcuts import render
from healthylife import settings
from healthylifeapp import views as general_views
from shop import views as shop_views

import requests
import json

# Nutrition views
def nutrition(request):
    """
    View for nutrition section
    Search nutritional information
    """
    food_information = None

    nutrition_filter_form = getNutritionFilterForm(request)

    if nutrition_filter_form.is_valid():
        food_name = nutrition_filter_form.cleaned_data['name']
        print(food_name)
    else:
        food_name = None

    if food_name is not None:
        food_information = getNutritionixApiInformation(food_name)
        #food_information = json.loads(food_information)
        print(food_information)

    shoppingcart = shop_views.getShoppingCart(request.session)

    return render(request, 'nutrition.html', {
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'search_food_form': getNutritionFilterForm(request),
        'food_information': food_information,
        'shoppingcart': shoppingcart,
    })


# Common Functions
def getNutritionFilterForm(request):
    """
    Method to get search food form
    depends that get or post request
    """
    if request.method == 'POST':
        nutrition_filter_form = nutrition_forms.NutritionFilter(request.POST)
    else:
        nutrition_filter_form = nutrition_forms.NutritionFilter()

    return nutrition_filter_form


def getNutritionixApiInformation(food):
    """
    Method that request on nutrition api
    """

    url = "https://trackapi.nutritionix.com/v2/search/instant?"
    """
    Populate any search interface, including autocomplete, with common foods and branded foods from Nutritionix. This searches our entire database of 600K+ foods.  Once a user selects the food from the autocomplete interface, make a separate API request to look up the nutrients of the food.
    https://gist.github.com/mattsilv/6d19997bbdd02cf5337e9d4806b4f464
    """

    url2 = "https://trackapi.nutritionix.com/v2/natural/nutrients?"
    """
    Get detailed nutrient breakdown of any natural language text
    https://gist.github.com/mattsilv/9dfb709e7609537ffd3b1b8c097e9bfb
    https://gist.github.com/mattsilv/95f94dd1378d4747fb68ebb2d042a4a6
    """

    url3 = "https://trackapi.nutritionix.com/v2/search/item?"
    """
    Look up the nutrition information for any branded food item by the nix_item_id (from /search/instant endpoint) or UPC scanned from a branded grocery product.
    https://gist.github.com/mattsilv/478c9288f213ce5333399a41bd6da5a4
    """

    body = {
      'query': food,
    }
    headers = {
        'x-app-id': settings.X_APP_ID,
        'x-app-key': settings.X_APP_KEY,
        #'x-remote-user-id': "7a43c5ba-50e7-44fb-b2b4-bbd1b7d22632",
    }
    response = requests.request("GET", url, params=body, headers=headers)
    #content = response.json()['common']
    content = response.json()
    # revisar aparte del common

    return content
