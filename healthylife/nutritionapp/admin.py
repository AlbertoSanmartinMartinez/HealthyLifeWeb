#!/usr/local/bin/python
# coding: utf-8

from __future__ import unicode_literals
from nutritionapp import models as nutrition_models
from django.contrib import admin

# Admin Nutrition Models
admin.site.register(nutrition_models.Food)
admin.site.register(nutrition_models.Measure)
admin.site.register(nutrition_models.MacroNutrient)
admin.site.register(nutrition_models.Dish)
admin.site.register(nutrition_models.Diet)
admin.site.register(nutrition_models.UserHealthProfile)
admin.site.register(nutrition_models.MicroNutrient)
