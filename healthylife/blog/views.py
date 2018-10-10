# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger

from blog import models as blog_models
from blog import forms as blog_forms
from healthylifeapp import models as general_models
from healthylifeapp import views as general_views
from shop import views as shop_views

# Blog Views
def list_posts(request, blog_category_slug=None):

    category = None
    posts = blog_models.Post.objects.filter(status=1)
    # blog_filter_form = None

    if blog_category_slug:
        category = get_object_or_404(blog_models.Category, slug=blog_category_slug)
        post = posts.filter(category=category)

    if request.method == 'POST':
        blog_filter_form = blog_forms.PostFilter(request.POST)
        if blog_filter_form.is_valid():
            data = blog_filter_form.cleaned_data
            if data['title'] is not None:
                print(data['title'])
                posts = posts.filter(
                    Q(title__icontains=data["title"]) |
                    Q(description__icontains=data["title"]) |
                    Q(tags__name__icontains=data["title"]))
            if data['category'] is not None:
                print("categoria introducido")
                posts = posts.filter(category_id=data['category'].id)
            """
            if data['minimum_date'] is not None:
                print("fecha minima introducido")
                posts = posts.filter(created_date__gte=data['minimum_date'])
            if data['maximum_date'] is not None:
                print("fecha maxima introducido")
                posts = posts.filter(created_date__lte=data['maximum_date'])
            """
            if data['order_by'] == 1:
                print("ordenacion introducido")
                posts = posts.all().order_by('created_date')
                #posts = posts.all().order_by('-created_date')
        else:
            print(blog_filter_form.errors)

    else:
        blog_filter_form = blog_forms.PostFilter()

    posts = posts.all().order_by('-created_date')
    #print(posts)

    paginator = Paginator(posts, 12)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    shoppingcart = shop_views.getShoppingCart(request.session)

    return render(request, "post_list.html", {
        'category': category,
        "posts": posts,
        #"categories": getBlogCategories(),
        'blog_filter_form': blog_filter_form,
        #'shoppingcart_form': getShoppingCart(),
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'shoppingcart': shoppingcart,
    })


def detail_post(request, post_slug):
    post = get_object_or_404(blog_models.Post, slug=post_slug)
    comments = blog_models.Comment.objects.filter(post=post.id, status=1, parent_id__isnull=True).order_by("created_date")
    images = general_models.Image.objects.filter(album=post.album)
    blog_filter_form = blog_forms.PostFilter()
    num_comments = len(blog_models.Comment.objects.filter(post=post.id, status=1))
    #related_posts = related_posts(post.title, post.category, post.tags, post.author)

    shoppingcart = shop_views.getShoppingCart(request.session)

    comment_form = getCommentForm(request)

    return render(request, "post_detail.html", {
        # 'comment_parent_id': 1,
        "post": post,
        "related_posts": related_posts(post_slug),
        "images": images,
        #"categories": getBlogCategories(),
        "comments":comments,
        "num_comments": num_comments,
        "comment_form": comment_form,
        #"answer_form": getCommentForm(request),
        'blog_filter_form': blog_filter_form,
        #'shoppingcart_form': getShoppingCart(),
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'shoppingcart': shoppingcart,
    })


def category_posts(request, category):
    category = blog_models.Category.objects.get(slug=category)
    posts = blog_models.Post.objects.filter(status=1, category=category.id)

    shoppingcart = shop_views.getShoppingCart(request.session)

    return render(request, 'post_list.html', {
        "posts":posts,
        "categories": getBlogCategories(),
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'shoppingcart': shoppingcart,
    })


def author_posts(request, username):
    author = User.objects.get(username=username)
    posts = blog_models.Post.objects.filter(status=1, author=author.id)
    categories = blog_models.Category.objects.order_by("name")

    shoppingcart = shop_views.getShoppingCart(request.session)

    return render(request, 'post_list.html', {
        "posts":posts,
        "categories": getBlogCategories(),
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'shoppingcart': shoppingcart,
    })


def tag_posts(request, tag_slug):
    print(tag_slug)
    tag = blog_models.Tag.objects.filter(slug=tag_slug)
    print(tag)
    posts = blog_models.Post.objects.filter(status=1, tags=tag)

    shoppingcart = shop_views.getShoppingCart(request.session)

    return render(request, 'post_list.html', {
        "posts":posts,
        "categories": getBlogCategories(),
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'shoppingcart': shoppingcart,
    })


def last_posts():

    return blog_models.Post.objects.filter(status=1).order_by('-created_date')[:6]


def related_posts(post_slug):
    post = get_object_or_404(blog_models.Post, slug=post_slug)
    #tags = blog_models.Tag.objects.filter(post_id=post.id)
    related_posts = blog_models.Post.objects.filter(
        Q(status=1) |
        Q(author=post.author) |
        Q(category=post.category))
        #Q(tags__in=tags))

    print(post.title)
    print(post.category)
    #print(post.tags)
    print(post.author)

    return related_posts

# Comments Views
def add_comment(request, post_slug):
    """
    Method that add comment to post:
    - from existing user and new user
    - new comments and answers
    If user is new add it to subscribers list
    """
    post = get_object_or_404(blog_models.Post, slug=post_slug)
    comment_form = getCommentForm(request)
    name = None
    comment_parent = None


    try:
        comment_parent_id = int(request.POST['comment_parent_id'])
    except:
        comment_parent_id = None


    if comment_form.is_valid():
        data = comment_form.cleaned_data

        if request.user.is_authenticated():
            name = request.user.username
        else:
            user = User.objects.filter(email=data['email'])
            if not user:
                general_models.Subscriber.objects.update_or_create(email=data['email'])
                name = data['name']
            else:
                name = user.username

        if comment_parent_id:
            comment_parent = blog_models.Comment.objects.get(id=str(comment_parent_id))
            if comment_parent:
                comment_parent_id = comment_parent.id

        blog_models.Comment.objects.create(
            status=2,
            title=data['title'],
            content=data['content'],
            author=name,
            post=post,
            parent=comment_parent)

    return redirect('blog:detail_post', post_slug=post.slug)


def delete_comment(request, comment_id):
    print("funcion que borrar un comentario")
    print(comment_id)
    comment = get_object_or_404(blog_models.Comment, id=comment_id)
    post = get_object_or_404(blog_models.Post, id=comment.post.id)
    print(comment)
    print(post)
    comment.delete()

    return redirect('blog:detail_post', post_slug=post.slug)


# Common Functions
def getBlogCategories():
    return blog_models.Category.objects.filter(parent__isnull=True).order_by("name")


def getCommentForm(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return blog_forms.CommentFormAuthenticated(request.POST)
        else:
            return blog_forms.CommentFormNotAuthenticated(request.POST)
    else:
        if request.user.is_authenticated:
            return blog_forms.CommentFormAuthenticated()
        else:
            return blog_forms.CommentFormNotAuthenticated()











#
