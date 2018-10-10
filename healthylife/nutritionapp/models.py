# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.timezone import datetime
from django.db import models
from django.contrib.auth.models import User

# Nutrition models
class UserHealthProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    SexType = ((0, ""), (1, "Hombre"), (2, "Mujer"))
    age = models.IntegerField(default=18)
    size = models.IntegerField(default=175)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    sport_frecuency = models.DecimalField(max_digits=4, decimal_places=3)
    sex = models.IntegerField(choices=SexType, default=0)

    def __unicode__(self):
        return str(self.user.username)

    def calculateSportFrecuency(slef, sport_day):
        pass


class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField(datetime.today)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def addIngredient(self):
        pass


class Measure(models.Model):
    """puede ser conveniente un campo de eleccion multiple antes que una clase"""
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class MicroNutrient(models.Model):
    pass


class MacroNutrient(models.Model):
    MacroNutrientType = ((1, "Proteinas"), (2, "Hidratos"), (3, "Grasas"), (2, "Fibra"))
    type = models.IntegerField(choices=MacroNutrientType, default=0)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    # fats = models.ForeignKey(Nutrient, default='')
    # carbohydrates = models.ForeignKey(Nutrient)
    # proteins = models.ForeignKey(Nutrient)
    # fiber = models.ForeignKey(Nutrient)
    # sodium = models.ForeignKey(Nutrient)
    # calories = models.ForeignKey(Nutrient)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Diet(models.Model):
    DietType = ((1, "Definicion"), (2, "Volumen"), (3, "Mantenimiento"), (2, "Adelgazamiento"))
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.IntegerField(choices=DietType, default=0)
    calories = models.IntegerField(default=18)
    days = models.IntegerField(default=90)
    # fechas

    def __unicode__(self):
        return "Dieta de " + str(self.user.username)
