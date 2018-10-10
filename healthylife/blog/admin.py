#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from blog import models as blog_models

# Admin Blog Models
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'updated_date', 'parent', 'author')
    list_filter = ('author',)
    search_fields = ('name', 'description')
    list_editable = ('name', 'parent')
    readonly_fields = ('slug', 'author', 'updated_date')

    def get_queryset(self, request):
        """
        Show only categories created by user
        """
        queryset = super(CategoryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(author_id=request.user.id)

    def save_model(self, request, obj, form, change):
        """
        Save the user that create the category as author
        """
        if not obj.author:
            obj.author = request.user
        obj.save()

admin.site.register(blog_models.Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created_date', 'title', 'category', 'author')
    list_filter = ('status', 'category', 'author')
    search_fields = ('title', 'description',)
    list_editable = ('status', 'title', 'category')
    readonly_fields = ('album', 'slug', 'author', 'created_date', 'updated_date')

    """
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(PostAdmin, self).save_model(request, obj, form, change)
    """

    def get_queryset(self, request):
        """
        Show only posts created by user
        """
        queryset = super(PostAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(author_id=request.user.id)

    def save_model(self, request, obj, form, change):
        """
        Save the user that create the post as author
        """
        if not obj.author:
            obj.author = request.user
        obj.save()


admin.site.register(blog_models.Post, PostAdmin)


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('author', 'updated_date', 'slug')

    def get_queryset(self, request):
        queryset = super(TagsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(author_id=request.user.id)

    def save_model(self, request, obj, form, change):
        """
        Save the user that create a tag as author
        """
        if not obj.author:
            obj.author = request.user
        obj.save()

admin.site.register(blog_models.Tag, TagsAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'title', 'author', 'post', 'parent')
    list_editable = ('status',)
    list_filter = ('status', 'parent')
    search_fields = ('title', 'content',)
    readonly_fields = ('author', 'updated_date')

    def get_queryset(self, request):
        queryset = super(CommentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        posts = blog_models.Post.objects.filter(author_id=request.user.id)
        return queryset.filter(post_id__in=posts)


admin.site.register(blog_models.Comment, CommentAdmin)





#
