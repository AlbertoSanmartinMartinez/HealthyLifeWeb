# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt

from blog import models as blog_models
from shop import models as shop_models
from api import serializers
from healthylifeapp import forms as general_forms

from rest_framework import permissions, generics, status #, authentication, exceptions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated


# Blog Api Views
def api_list_posts(request):
    print("vista del blog de la api")

    if request.method == 'GET':
        posts = blog_models.Post.objects.filter(status=1)
        posts = serializers.PostSerializer(posts, many=True)
        # print(posts.data)

        return JsonResponse(posts.data, safe=False)

"""
class APIPostList(generics.ListAPIView):
    serializer_class = serializers.PostSerializer
    queryset = blog_models.Post.objects.all()

    class Meta:
        model = blog_models.Post
        fields = "__all__"
"""

class APIPostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PostSerializer
    # model = blog_models.Post

    def get_queryset(self, *args, **kwargs):
        status = self.request.query_params.get('status', None)
        if status:
            queryset = blog_models.Post.objects.filter(status=status)
            return queryset

    class Meta:
        model = blog_models.Post
        fields = "__all__"


class APICategoryList(generics.ListAPIView):
    queryset = blog_models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    class Meta:
        model = blog_models.Category
        fields = "__all__"


class APICategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    # model = models.Category
    queryset = blog_models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        queryset = blog_models.Category.objects.all()
        queryset = queryset.filter(name=self.request.query_params.get('category_id'))


class APICommentList(generics.ListAPIView):
    queryset = blog_models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    class Meta:
        model = blog_models.Comment
        fields = "__all__"


class APICommentDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    # model = models.Category
    queryset = blog_models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class APITagList(generics.ListAPIView):
    serializer_class = serializers.TagSerializer
    queryset = blog_models.Tag.objects.all()

    class Meta:
        model = blog_models.Tag
        fields = "__all__"


# Shop Api Views
def api_list_products(request):
    print("vista de la tienda de la api")

    if request.method == 'GET':
        products = shop_models.Product.objects.filter(status=1)
        products = serializers.ProductSerializer(products, many=True)
        # print(posts.data)

        return JsonResponse(products.data, safe=False)

"""
class APIProductList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = shop_models.Product.objects.all()

    class Meta:
        model = shop_models.Product
        fields = "__all__"
"""

class APIProductDetail():
    serializer_class = serializers.ProductSerializer

    def get_queryset(self, *args, **kwargs):
        status = self.request.query_params.get('status', None)
        if status:
            queryset = shop_models.Product.objects.filter(status=status)
            return queryset


class APICategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = shop_models.Category.objects.all()

    class Meta:
        model = shop_models.Product
        fields = "__all__"


class APICategoryDetail():
    pass


class APIReviewList(generics.ListAPIView):
    serializer_class = serializers.ReviewSerializer
    queryset = shop_models.Review.objects.all()

    class Meta:
        model = shop_models.Review
        fields = "__all__"


class APIReviewDetail():
    pass


class APITagList(generics.ListAPIView):
    serializer_class = serializers.TagSerializer
    queryset = shop_models.Tag.objects.all()

    class Meta:
        model = shop_models.Tag
        fields = "__all__"


class APITagDetail():
    pass


# Awards Api Views
def api_list_awards(request):
    pass


# General Api Views
def api(request):
    return render(request, 'api.html', {})


@api_view(['GET'])
def custom_login_api(request):
    print("funcion para logear un usuario a través de la api")
    if request.method == 'GET':
        print('metodo get django')

        #data = JSONParser().parse(request)
        #print(data)
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        print(username)
        print(password)

        #user = authenticate(username=username, password=password)

        credentials = {
            get_user_model().USERNAME_FIELD: username,
            'password': password
        }

        user = authenticate(**credentials)

        if user is not None:
            print("user correcto")
            if user.is_active:
                login(request, user)
                return JsonResponse(user.data, status=201)
        else:
            return JsonResponse(user.errors, status=400)


@api_view(['POST'])
def custom_registration_api(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = general_forms.CustomRegisterForm(data=data)

        if user.is_valid():
            user.save()
            return JsonResponse(user.data, status=201)

        return JsonResponse(user.errors, status=400)



#@user_passes_test(lambda u: u.is_superuser)
class APIUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


#@user_passes_test(lambda u: u.is_superuser)
class APIUserDetail():
    pass










#
