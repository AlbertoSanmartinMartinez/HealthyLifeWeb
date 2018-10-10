#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
"""

from django.contrib import admin
from healthylifeapp import models
#from healthylifeapp import custom_calendar
from django.contrib.auth.models import Permission
#from taggit.managers import TaggableManager
# from rollyourown.seo.admin import register_seo_admin
# from myapp.seo import MyMetadata
# from collections import OrderedDict as SortedDict


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'description', 'alt', 'album')

class ImageInLine(admin.TabularInline):
    model = models.Image
    list_display = ('id', 'image', 'description', 'alt')
    extra = 1

admin.site.register(models.Image, ImageAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author')
    search_fields = ('name', 'author')
    inlines = [ImageInLine,]

    def save_model(self, request, obj, form, change):
        """
        Save the user that create the album as author
        """
        if not obj.author:
            obj.author = request.user
        obj.save()

    def get_queryset(self, request):
        queryset = super(AlbumAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(author_id=request.user.id)


admin.site.register(models.Album, AlbumAdmin)

# Admin Profile Models
admin.site.register(models.UserProfile)

class CollaboratorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'company', 'education', 'extract')

admin.site.register(models.CollaboratorProfile, CollaboratorProfileAdmin)

admin.site.register(models.Address)
admin.site.register(models.BankInformation)
admin.site.register(models.Company)


# Admin General Models
admin.site.register(models.Subscriber)
