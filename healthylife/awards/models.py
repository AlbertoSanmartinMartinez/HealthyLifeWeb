#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from healthylife.decorators import autoconnect
from django.contrib.auth.models import User
from shop import models as shop_models
from healthylifeapp import models as general_models
import datetime

# Awards models
@autoconnect
class Category(models.Model):
    """
    Model for awards categories
    """
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField()
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, editable=False, null=True, blank=True, related_name='award_category_author', on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name

    def pre_save(self, *args, **kwargs):
        """
        """
        self.slug = self.name.replace(" ", "_").lower()
        self.updated_date = datetime.datetime.now()


@autoconnect
class Award(models.Model):
    """
    modelo para los premios de los usuarios
    """
    Status = ((1, "Activo"), (2, "Inactivo"))
    status = models.IntegerField(choices=Status, default=2, blank=True)
    title = models.CharField(max_length=100, blank=False)
    slug = models.CharField(max_length=100, default=' ', blank=True)
    description = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    AwardType = ((1,'Porcentaje'), (2, 'Cantidad'))
    award_type = models.IntegerField(choices=AwardType, default=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    author = models.ForeignKey(User, editable=False, null=True, blank=True, related_name='award_author', on_delete=models.SET_NULL)
    album = models.ForeignKey(general_models.Album, blank=True, null=True, on_delete=models.SET_NULL)
    shop_objects = models.ManyToManyField(shop_models.Product, blank=True)
    users = models.ManyToManyField(User, related_name='Beneficiario', blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Award method that save the slug, updated date and create the award album
        """
        self.slug = self.title.replace(" ", "_").lower()
        self.updated_date = datetime.datetime.now()
        if not self.pk:
            album = general_models.Album.objects.create(name='Album Premio '+self.title, author=self.author, )
            self.album = album
            general_models.Image.objects.create(album=self.album, header_image=True, image='photos/header_award_default_image.jpg')
        general_models.Album.objects.filter(id=self.album.id).update(name='Album Premio ' + self.title)
        super(Award, self).save(*args, **kwargs)




    #
