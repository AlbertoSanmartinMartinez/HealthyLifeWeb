#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from events import models as event_models

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'privacity', 'type', 'title', 'owner', 'created_date', 'updated_date', 'start', 'end')
    list_filter = ('privacity', 'type', 'start', 'end')
    search_fields = ('title', 'owner', 'owner')

admin.site.register(event_models.Event, EventAdmin)
