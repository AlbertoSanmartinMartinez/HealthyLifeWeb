#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from healthylife.decorators import autoconnect
from django.contrib.auth.models import User
import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields
from django.utils import timezone

timezone.now()

# Event Models
@autoconnect
class Event(models.Model):
    """
    Clase para los eventos.
    """
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, default=' ', blank=True)
    description = models.CharField(max_length=250, blank=True)
    PrivacityType = ((1, 'Público'), (2, 'Privado'))
    privacity = models.IntegerField(choices=PrivacityType, default=1, blank=True)
    EVENT_TYPE = ((1, 'Deporte'), (2, 'Nutrición'), (3, 'Salud'))
    type = models.IntegerField(choices=EVENT_TYPE, default=1)
    owner = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    created_date = models.DateTimeField(auto_now=True)
    updated_date= models.DateTimeField()
    participant = models.ManyToManyField(User, related_name='participants', blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    address = models.CharField(max_length=250, default='', blank=True)
    notes = models.CharField(max_length=250, default='', blank=True)

    def __unicode__(self):
        return self.title

    def save(self):
        """
        Metodo para aignar el slug de un evento automaticamente al crearlo
        """
        self.slug = self.title.replace(" ", "_").lower()
        self.updated_date = datetime.datetime.now()

    def inviteParticipants(self):
        """
        Metodo que envia un correo a un usuario para que se una al evento
        """
        pass


# Sport Event
# Nutrition Event
# Health Event
