#!/usr/local/bin/python
# coding: utf-8

from django import template
from django.shortcuts import render
from shop import models as shop_models

register = template.Library()

@register.simple_tag
def calculateStockItem(product_id):
    product = shop_models.Product.objects.filter(id=product_id)

    return product.stock

@register.simple_tag
def getHeaderImage(product_id):
    product = shop_models.Product.objects.get(id=product_id)
    picture = shop_models.Image.objects.get(header_image=True, album=product.album)

    return picture

@register.simple_tag
def getImages(product_id):
    product = shop_models.Product.objects.get(id=product_id)
    pictures = shop_models.Image.objects.filer(header_image=False, album=product.album)

    return picture


@register.simple_tag
def get_user_image(username):
    """
    Method that return user profile image from user
    """
    user_profile = None
    print("funcion para obtener la foto")
    print(username)
    try:
        user = User.objects.filter(username=username)
    except:
        user = None
    if user:
        user_profile = general_models.UserProfile.objects.get(user_id=user)
        print(user_profile.profile_image)

    return user_profile
