#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django import template
from events import models as events_models
import datetime
from calendar import monthrange

register = template.Library()

@register.simple_tag
def getEvents(user_id, year, month, day, type=None):
    day = int(day)
    year = int(year)
    month = int(month)
    # filtar los eventos en los que participa
    # filtar los eventos públicos de su zona

    min_date = datetime.datetime(year, month, day, 0, 0)
    max_date = datetime.datetime(year, month, day, 23, 59)

    events = events_models.Event.objects.filter(owner=user_id, start__range=(min_date, max_date)).order_by('start')

    return events

@register.simple_tag
def isMultipleBiggerThanZero(number):
    if number % 7 == 0:
        if number > 0:
            return True
    else:
        return False


@register.simple_tag
def isToday(year, month, day):
    today = datetime.datetime.now()
    if int(year) == int(today.year) and int(month) == int(today.month) and int(day) == int(today.day):
        return True
