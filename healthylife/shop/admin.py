#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from shop import models as shop_models

# Admin Shop Models
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'name', 'created_date', 'category', 'stock', 'price']
    list_filter = ['status', 'category']
    list_editable = ['status', 'category', 'stock', 'price']
    search_fields = ['name', 'description']
    readonly_fields = ('slug', 'author', 'album', 'updated_date')
    # prepopulated_fields

    """
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(ProductAdmin, self).save_model(request, obj, form, change)
    """

    def get_queryset(self, request):
        """
        Show only products created by user
        """
        queryset = super(ProductAdmin, self).get_queryset(request)
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

admin.site.register(shop_models.Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent'] #, 'author']
    # list_filter = ['author',]
    search_fields = ['name', 'description', 'parent']
    list_editable = ['name', 'parent']
    # readonly_fields = ['slug', 'author', 'updated_date']
    # prepopulated_fields

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

admin.site.register(shop_models.Category, CategoryAdmin)


class ShopingChartAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'code', 'created_date', 'products']

admin.site.register(shop_models.ShopingChart, ShopingChartAdmin)

"""
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']

admin.site.register(shop_models.Provider, ProviderAdmin)
"""

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

admin.site.register(shop_models.Tag, TagsAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['code', 'created_date', 'status']

admin.site.register(shop_models.Order, OrderAdmin)

"""
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'description', 'alt', 'album')

class ImageInLine(admin.TabularInline):
    model = models.Image
    list_display = ('id', 'image', 'description', 'alt')
    extra = 1

admin.site.register(models.Image, ImageAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    inlines = [ImageInLine,]

admin.site.register(models.Album, AlbumAdmin)
"""

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'title', 'created_date', 'author', 'product', 'parent')
    list_editable = ('status', 'author')
    list_filter = ('status', 'parent')
    search_fields = ('title', 'content', 'author', 'product')

    def get_queryset(self, request):
        """
        Show only comments from the post created by user
        """
        queryset = super(ReviewAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        products = shop_models.Product.objects.filter(author_id=request.user.id)
        return queryset.filter(product_id__in=products)

admin.site.register(shop_models.Review, ReviewAdmin)

"""
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'amount')

admin.site.register(shop_models.Discount, DiscountAdmin)
"""

admin.site.register(shop_models.Shipping)
