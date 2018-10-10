# coding: utf-8

from django.conf.urls import url
from django.urls import path, include

from api import views as api_views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [

    path('', api_views.api, name='api_home'),

    # API Blog URLS
    # path(r'^blog/posts/$', api_views.APIPostList.as_view(), name='post-list'),
    path('blog/posts/', api_views.api_list_posts, name='post-list'),
    # path(r'^api/posts/(?P<pk>\d+)/$', blog_views.APIPostDetail.as_view(), name='post-detail'),

    path('blog/categories/', api_views.APICategoryList.as_view(), name='category-list'),
    # path(r'^api/categories/(?P<pk>\d+)/$', blog_views.APICategoryDetail.as_view(), name='category-detail'),

    path('blog/comments/', api_views.APICommentList.as_view(), name='comment-list'),
    # path(r'^api/comments/(?P<pk>\d+)/$', blog_views.APICommentDetail.as_view(), name='comment-detail'),

    path('blog/tags/', api_views.APITagList.as_view(), name='tag-list'),
    # path(r'^api/tags/(?P<pk>\d+)/$', blog_views.APITagDetail.as_view(), name='tag-detail'),

    # path(r'^users/$', blog_views.APIUserList.as_view(), name='user-list'),
    # path(r'^users/(?P<pk>\d+)/$', blog_views.APIUserDetail.as_view(), name='user-detail'),

    # path(r'^users/login$', blog_views.userLoginAPI, name='user-login-api'),
    # path(r'^users/register/$', blog_views.userRegistrationAPI, name='user-register-api'),


    # API Shop URLS
    path('shop/products/', api_views.api_list_products, name='product-list'),
    #path(r'^api/products/$', blog_views.APIProductList.as_view(), name='product-list'),

    path('shop/categories/', api_views.APICategoryList.as_view(), name='category-list'),
    #path(r'^api/products/$', blog_views.APIProductList.as_view(), name='category-detail'),

    path('shop/reviews/', api_views.APIReviewList.as_view(), name='review-list'),
    #path(r'^api/products/$', blog_views.APIProductList.as_view(), name='review-detail'),

    path('shop/tags/', api_views.APIReviewList.as_view(), name='tag-list'),
    #path(r'^api/products/$', blog_views.APIProductList.as_view(), name='tag-detail'),

    # API Blog URLS
    path('awards/', api_views.api_list_awards, name='awards-list'),

    # API General URLS
    path('users/', api_views.APIUserList.as_view(), name='user-list'),
    path('users/register/', api_views.custom_registration_api, name='user-register'),
    path('api-token-auth/', obtain_jwt_token),

]











#
