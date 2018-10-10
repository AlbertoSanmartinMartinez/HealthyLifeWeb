# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.timezone import datetime
from django.db import models

# Sport models
class SportType(models.Model):
    """puede ser conveniente un campo de eleccion multiple antes que una clase"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __unicode__(self):  # python 2
        return self.name


class SportSession(models.Model):
    name = models.CharField(max_length=100)
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE)
    date = models.DateField(datetime.today)
    # usuario = models.ForeignKey(User)
    duration = models.TimeField()
    calories = models.IntegerField()

    def __unicode__(self):  # python 2
        return self.name

    def __str__(self):  # python 3
        return self.name
