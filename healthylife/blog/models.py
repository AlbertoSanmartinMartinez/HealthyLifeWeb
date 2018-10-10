#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from healthylife.decorators import autoconnect
from healthylifeapp import models as general_models

import datetime

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Blog models
class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=50, unique=True)
    slug = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(User, editable=False, null=True, blank=True, related_name='blog_tag_author', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        metodo de la clase Tag para calcular el slug de una etiqueta y actualizar la fecha de creación
        """
        self.slug = self.name.replace(" ", "_").lower()
        self.updated_date = datetime.datetime.now()
        super(Tag, self).save(*args, **kwargs)


@autoconnect
class Category(models.Model):
    """Modelo para las categorias del blog"""
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField()
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, editable=False, null=True, blank=True, related_name='post_category_author', on_delete=models.CASCADE)

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


class PostType(models.Model):
    pass
    # nombre
    # plantilla


@autoconnect
class Post(models.Model):
    """Modelo para los articulos del blog"""
    Status = ((1, "Publicado"), (2, "Borrador"), (3, "Eliminado"))
    status = models.IntegerField(choices=Status, default=2, blank=True)
    title = models.CharField(max_length=100, blank=False)
    slug = models.CharField(max_length=100, default='', blank=True)
    description = models.CharField(max_length=200, blank=False)
    content = RichTextUploadingField('content', config_name='full')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    author = models.ForeignKey(User, editable=False, null=True, blank=True, related_name='post_author', on_delete=models.SET_NULL)
    album = models.ForeignKey(general_models.Album, default=1, blank=True, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, related_name='post_tags')


    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        metodo de la clase post para calcular el slug de un post y crear un album asociado a ese post
        """
        self.slug = self.title.replace(" ", "_").lower()
        self.updated_date = datetime.datetime.now()
        if not self.pk:
            self.created_date = datetime.datetime.now()
            album = general_models.Album.objects.create(name='album ' + self.title, author=self.author)
            self.album = album
            general_models.Image.objects.create(album=self.album, header_image=True, image='photos/header_post_default_image.jpg')
        general_models.Album.objects.filter(id=self.album.id).update(name='Album Post ' + self.title)
        super(Post, self).save(*args, **kwargs)

    def publishPost(self):
        """metodo de la clase post para publicar en redes sociles un post"""
        pass


@autoconnect
class Comment(models.Model):
    """
    https://stackoverflow.com/questions/44837733/how-to-make-add-replies-to-comments-in-django
    """
    Status = ((1, "Publicado"), (2, "Pendiente de Revision"), (3, "Eliminado"))
    status = models.IntegerField(choices=Status, default=2)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField()
    author = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='answers', null=True, blank=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated_date = datetime.datetime.now()
        super(Comment, self).save(*args, **kwargs)

    def post_save(self, **kwargs):
        pass
        # self.notifyNewComment()

    def notifyNewComment(self):
        self.status = 1
        print("notificacion enviada")



#
