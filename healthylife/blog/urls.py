#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from healthylife import settings
from blog import views as blog_views

urlpatterns = [

    # Blog URLS's
    path('posts/', blog_views.list_posts, name='list_post'),
    path('posts/', blog_views.list_posts, name='blog_search'),

    # hacer generica
    #path(r'^blog/subscripcion/$', blog_views.subscribe, name='subscribe'),

    path('posts/<str:post_slug>/', blog_views.detail_post, name='detail_post'),
    path('posts/<str:post_slug>/comentario', blog_views.add_comment, name='add_comment'),

    path('comentarios/<int:comment_id>/borrar/', blog_views.delete_comment, name='delete_comment'),

    # path(r'^blog/(?P<post_slug>\w+)/(?P<comment_parent_id>\w+)/comentado/$', views.comment, name='comment'),
    path('categorias/<str:category>/', blog_views.category_posts, name='category_posts'),
    path('autores/<str:username>/', blog_views.author_posts, name='author_posts'),
    path('etiquetas/<str:tag_slug>/', blog_views.tag_posts, name='tag_posts'),

]
