# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sportapp import models as sport_models
from django.contrib import admin

# Admin Sport Models
admin.site.register(sport_models.SportType)

class SportSessionAdmin(admin.ModelAdmin):
    model = sport_models.SportSession

admin.site.register(sport_models.SportSession, SportSessionAdmin)
