# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from healthylifeapp import views as general_views
from awards import forms as awards_forms
from shop import views as shop_views
from awards import models as award_models
from django.contrib.auth.models import User

# Award views
def awards(request):
    """
    """
    awards_filter_form = getAwardsFilterForm(request)
    awards = None

    shoppingcart = shop_views.getShoppingCart(request.session)

    return render(request, 'awards.html', {
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'awards_filter_form': getAwardsFilterForm(request),
        'awards': awards,
        'shoppingcart': shoppingcart,
    })


def award_detail(request, award_slug):
    """
    View for award details
    """
    award = award_models.Award.objects.filter(slug=award_slug)

    shoppingcart = shop_views.getShoppingCart(request.session)

    return render(request, 'award_detail.html', {
        'award': award,
        'awards_filter_form': getAwardsFilterForm(request),
        'subscribe_form': general_views.getSubscribeForm(),
        "search_form": general_views.getSearchForm(),
        'shoppingcart': shoppingcart,
    })


def best_awards():
    """
    Award view for best wards in home slide
    """

    return award_models.Award.objects.filter(status=1).order_by("-created_date")[:3]


def getAwardsFilterForm(request):
    """
    """
    if request.method == 'POST':
        nutrition_filter_form = awards_forms.AwardFilter(request.POST)
    else:
        nutrition_filter_form = awards_forms.AwardFilter()

    return nutrition_filter_form


def awards_profile(request, username):
    """
    View that returns the awards that a user has obtained
    """
    user = User.objects.filter(username=username)
    awards = award_models.Award.objects.filter(users=user)
    print("secion de premios del perfil")
    print(awards)

    shoppingcart = shop_views.getShoppingCart(request.session)

    return render(request, 'awards_profile.html', {
        'awards': awards,
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'shoppingcart': shoppingcart,
    })


def coupon(request):
    pass
