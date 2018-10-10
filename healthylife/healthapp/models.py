# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Health models
class Illnes(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
