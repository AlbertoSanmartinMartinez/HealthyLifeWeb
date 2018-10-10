#!/usr/local/bin/python
# coding: utf-8

from django import template
from django.shortcuts import render
from blog import models as blog_models
from healthylifeapp import models as general_models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def get_comment_answers(comment_parent):
    """
    Doesn´t use --> comment.answers.all
    Template tag method que busca las respuestas a un comentario
    """
    comment_answers = blog_models.Comment.objects.filter(status=1).order_by("-created_date")
    #print(comment_answers)

    return comment_answers if comment_answers else None


#register.filter('comment_answers', comment_answers)
@register.simple_tag
def get_user_image(username):
    """
    Method that return user profile image from user
    """

    try:
        user = get_object_or_404(user, username=username)
        user_profile = get_object_or_404(UserProfile, user_id=user.id)
    except:
        user_profile = None

    return user_profile


@register.simple_tag
def get_user_authenticated(request, username):
    """
    Method that check if an author of post is an user registered or not
    """
    try:
        user = get_object_or_404(User, username=username)
    except:
        user = None
    if user:
        if str(request.user) == str(user.username):
            return True

    return False







#
