#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.utils.timezone import datetime
from django.forms import ModelForm
from django.db.models import signals
from django.dispatch import receiver
from django.utils.text import slugify

from healthylife.decorators import autoconnect
from django.core.validators import URLValidator

#from taggit.managers import TaggableManager
from image_cropping import ImageRatioField
#from taggit.models import TagBase

# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFit

# General models
@autoconnect
class Address(models.Model):
    """Modelo para las direcciones postales"""
    address_name = models.CharField(max_length=50, default="Mi dirección de envío")
    city = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=5)
    street = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=4, blank=True)
    floor = models.CharField(max_length=3, blank=True)
    door = models.CharField(max_length=3, blank=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    is_company = models.BooleanField(default=False)

    def __unicode__(self):
        return self.address_name

    @receiver(signals.post_save, sender=User)
    def create_user_address(sender, instance, created, **kwargs):
        """este metodo crea la direccion postal y la informacion bancaria de un usuario"""
        if created:
            Address.objects.create(user_id=instance.id)

    def pre_save(self, **kwargs):
        """metodo de la clase Address para estandarizar los atributos"""
        self.address_name = self.address_name.capitalize()
        self.city = self.city.title()
        self.street = self.street.title()
        self.door = self.door.upper()


class BankInformation(models.Model):
    """
    Bank information model
    """
    bank_name = models.CharField(max_length=50, default="Mi información bancaria")
    account = models.CharField(max_length=20, blank=True)
    month = models.CharField(max_length=2, blank=True)
    year = models.CharField(max_length=4, blank=True)
    security_code = models.CharField(max_length=3, blank=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    is_company = models.BooleanField(default=False)

    def __unicode__(self):
        return self.bank_name

    def pre_save(self):
        """metodo de la clase BankInformation para estandarizar los atributos"""
        self.bank_name = self.bank_name.capitalize()

    @receiver(signals.post_save, sender=User)
    def create_user_bank_information(sender, instance, created, **kwargs):
        if created:
            BankInformation.objects.create(user_id=instance.id)


class UserProfile(models.Model):
    """Modelo para el perfil de un usuario"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100, blank=True)
    phone = models.CharField(max_length=9, blank=True)
    profile_image = models.ImageField(upload_to="photos", default='photos/user_profile.jpg', blank=True)
    cropping = ImageRatioField('profile_image', '390x450')

    def __unicode__(self):
        return str(self.user.username)

    @receiver(signals.post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        """Este metodo crea la direccion postal y la informacion bancaria de un usuario"""
        if created:
            UserProfile.objects.create(user_id=instance.id)


class CollaboratorProfile(models.Model):
    """Modelo para el perfil de un colaborador"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, default='', blank=True)
    company = models.CharField(max_length=50, default='', blank=True)
    education = models.CharField(max_length=50, default='', blank=True)
    extract = models.TextField(default=' ', blank=True)
    collaborator_image = models.ImageField(upload_to="photos", default='photos/user_profile.jpg', blank=True)
    cropping = ImageRatioField('collaborator_image', '390x450')

    def __unicode__(self):
        return self.user.username


class Subscriber(models.Model):
    email = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.email


# Statistics models

# Gallery models
@autoconnect
class Album(models.Model):
    name = models.CharField(max_length=50, default='album')
    #slug = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(User, default=3, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(" ", "_").lower()
        super(Album, self).save(*args, **kwargs)


class Image(models.Model):
    """
    Modelo para las fotos
    https://stackoverflow.com/questions/765396/exif-manipulation-library-for-python
    """
    album = models.ForeignKey(Album, default=1, on_delete=models.CASCADE)
    header_image = models.BooleanField(default=False)
    image = models.ImageField(upload_to="photos", default='/image.jpg', blank=False)
    # image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 90})
    description = models.CharField(max_length=20, blank=True)
    alt = models.CharField(max_length=20, blank=True) # texto alternativo alt=""
    # tamaño (jpeg)
    # datos exif
    # sitemap de imagenes

    def __unicode__(self):
        return unicode(self.image)



@autoconnect
class Company(models.Model):
    """modelo para las empresa de la tienda"""
    company_name = models.CharField(max_length=50, default='mi empresa')
    slug = models.CharField(max_length=100, default=' ', blank=True)
    description = models.CharField(max_length=100, default=' ', blank=True)
    phone = models.CharField(max_length=9, default='000000000', blank=True)
    web =  models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    company_image = models.ImageField(upload_to="photos", default='photos/default_company_image.jpg', blank=True)
    cropping = ImageRatioField('company_image', '160x160')

    def __unicode__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        """metodo de la clase company para calcular el slug"""
        self.slug = self.company_name.replace(" ", "_").lower()
        super(Company, self).save(*args, **kwargs)


# SEO models
class MetaData(models.Model):
    pass
