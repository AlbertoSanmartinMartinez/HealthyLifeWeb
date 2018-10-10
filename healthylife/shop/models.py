# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from payments import PurchasedItem
from payments.models import BasePayment
from healthylife.decorators import autoconnect
from healthylifeapp import models as general_models
from django.contrib.auth.models import User
import datetime

# Shop Models
class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=50, unique=True)
    slug = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(User, editable=False, null=True, blank=True, related_name='shop_tag_author', on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(default=datetime.datetime.now())

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
    """
    Model for categories from a shop
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.CharField(max_length=500, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, related_name='category_author', editable=False, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name

    def pre_save(self, **kwargs):
        """
        """
        self.slug = self.name.replace(" ", "_").lower()
        self.updated_date = datetime.datetime.now()


@autoconnect
class Product(models.Model):
    Status = ((1, "Activo"), (2, 'Inactivo'))
    status = models.IntegerField(choices=Status, default=2, blank=True)
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=100, db_index=True, unique=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, blank=True)
    description = models.CharField(max_length=500, blank=True)
    # contenido
    updated_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # professional_prize
    album = models.ForeignKey(general_models.Album, default=1, blank=True, null=True, on_delete=models.SET_NULL)
    # color
    Size = ((1, "XS"), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL'))
    size = models.IntegerField(choices=Size, default=1, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0) # revisar peso de los productos
    # award = models.ForeignKey(award_models.Award, blank=True, null=True)
    author = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, related_name='shop_tags')

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        metodo de la clase post para calcular el slug de un producto y crear un album asociado a ese producto
        """
        self.slug = self.name.replace(" ", "_").lower()
        self.updated_date = datetime.datetime.now()
        if not self.pk:
            album = general_models.Album.objects.create(name='Album Producto '+self.name, author=self.author)
            self.album = album
            general_models.Image.objects.create(album=self.album, header_image=True, image='photos/header_product_default_image.jpg')
        general_models.Album.objects.filter(id=self.album.id).update(name='Album Product ' + self.name)
        super(Product, self).save(*args, **kwargs)


@autoconnect
class Review(models.Model):
    """Modelo para los comentarios de la tienda"""
    Status = ((1, "Publicado"), (2, "Pendiente de Revision"), (3, "Eliminado"))
    status = models.IntegerField(choices=Status, default=2, blank=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey('self', related_name='answers', null=True, blank=True, on_delete=models.SET_NULL)
    mark = models.IntegerField(default=10)

    def __unicode__(self):
        return self.title

    def post_save(self, **kwargs):
        pass
        #self.notifyNewComment()

    def notifyNewComment(self):
        """Metodo que avisa de un nuevo comentario en el blog"""
        self.status = 1
        print("notificacion enviada")


# ShoppinCart Models
class ShopingChart(models.Model):
    # name = models.CharField(max_length=100, db_index=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=300, default="", unique=True)
    products = models.CharField(max_length=300, default="")
    STATUS = ((1, 'Activo'), (2, 'Abandonado'))
    status = models.IntegerField(choices=STATUS, default=1)
    # controlar el estado del carrito
    # convertir en pedido cuando se finaliza el pedido
    # saber de quien es el carrito

    def __unicode__(self):
        return self.code


# Order Models
# https://www.wordstream.com/blog/ws/2016/03/17/shopping-cart-abandonment
class Order(models.Model):
    """
    - enviar por correo electronico
    - generar factura
    """
    code = models.CharField(max_length=300, default="")
    created_date = models.DateTimeField(auto_now=True)
    OrderStatus = ((1, 'Pendiente de pago'), (2, 'Cancelado'), (3, 'Pagado'), (4, 'En preparación'), (5, 'Enviado'), (6, 'Entregado'))
    status = models.IntegerField(choices=OrderStatus, default=1)
    # pedidos para cada empresa

    def __unicode__(self):
        return self.code


# SEO Models
class MetaData(models.Model):
    pass


# Payment Models


# Shipping Models
class Shipping(models.Model):
    """
    https://django-oscar.readthedocs.io/en/releases-1.0/index.html

    """
    company = models.CharField(max_length=100)
    #max_weight = models.IntegerField()
    #max_num_items = models.IntegerField()
    COUNTRIES = ((1,'España'),)
    country = models.IntegerField(choices=COUNTRIES, default=1)
    REGIONS = ((1,'Aragon'),)
    region = models.IntegerField(choices=REGIONS, default=1)
    PROVINCES = ((1,'España'),)
    province = models.IntegerField(choices=PROVINCES, default=1)
    TIME = ((1,'24h'), (2, '48h'))
    time = models.ImageField(choices=TIME, default=1)

    def __unicode__(self):
        return self.company








"""
https://www.youtube.com/watch?v=Z5dBopZWOzo
https://django-payments.readthedocs.io/en/latest/index.html

"""
