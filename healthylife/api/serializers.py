#!/usr/local/bin/python
# coding: utf-8

#from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer
from rest_framework import fields

from blog import models as blog_models
from shop import models as shop_models
from healthylifeapp import models as general_models

from django.contrib.auth.models import User

# Blog Serializers
class CategorySerializer(ModelSerializer):

    class Meta:
        model = blog_models.Category
        fields = "__all__"


class PostSerializer(ModelSerializer):

    class Meta:
        model = blog_models.Post
        fields = "__all__"


class CommentSerializer(ModelSerializer):

    class Meta:
        model = blog_models.Comment
        fields = "__all__"


class TagSerializer(ModelSerializer):

    class Meta:
        model = blog_models.Tag
        fields = "__all__"


# Shop Serializers
class ProductSerializer(ModelSerializer):

    class Meta:
        model = shop_models.Product
        fields = "__all__"

class ReviewSerializer(ModelSerializer):

    class Meta:
        model = shop_models.Review
        fields = "__all__"


class TagSerializer(ModelSerializer):

    class Meta:
        model = shop_models.Tag
        fields = "__all__"


class CategorySerializer(ModelSerializer):

    class Meta:
        model = shop_models.Category
        fields = "__all__"


# General Serializers
"""
http://blog.enriqueoriol.com/2015/03/django-rest-framework-serializers.html
"""
class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = general_models.UserProfile
        fields = "__all__"







#
