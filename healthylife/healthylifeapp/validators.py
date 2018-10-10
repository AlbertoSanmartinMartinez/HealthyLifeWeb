#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

from healthylife import settings

def custom_image_file_validator(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

"""
def get_default_password_validators():
    return get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)
"""

class NumberValidator(object):

    def __init__(self, min_digits=0):
        self.min_digits = min_digits

    def validate(self, password, user=None):
        print("llega a la funcion")
        if not len(re.findall('\d', password)) >= self.min_digits:
            raise ValidationError(
                _("Tu contraseña debe contener al menos %(min_digits)d dígito entre 0 y 9."),
                code='password_no_number',
                params = {'min_digits': self.min_digits},
            )

    def get_help_text(self):
        return _(
            "Tu contraseña debe contener al menos %(min_digits)d dígito entre 0 y 9." % {'min_digits': self.min_digits}
        )


class UppercaseValidator(object):

    def __init__(self, min_uper=0):
        self.min_uper = min_uper

    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("Tu contrasena debe contener al menos 1 mayuscula."),
                code='password_no_upper',
                #params = {'min_uper': self.min_uper},
            )
    """
    def get_help_text(self):
        return _(
            "Tu contraseña debe contener al menos 1 mayuscula."
        )
    """

class LowercaseValidator(object):

    def __init__(self, min_lower=0):
        self.min_lower = min_lower

    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("Tu contrasena debe contener al menos 1 minuscula."),
                code='password_no_lower',
                #params = {'min_lower': self.min_lower},
            )

    def get_help_text(self):
        return _(
            "Tu contrasena debe contener al menos 1 minuscula."
        )


class SymbolValidator(object):

    def __init__(self, min_char=0):
        self.min_char = min_char

    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&amp;*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("Tu contrasena debe contener al menos 1 caracter de esta lista: " +
                  "()[]{}|\`~!@#$%^&amp;*_-+=;:'\",<>./?"),
                code='password_no_symbol',
                #params = {'min_char': self.min_char},
            )

    def get_help_text(self):
        return _(
            "Tu contrasena debe contener al menos 1 caracter de esta lista: " +
            "()[]{}|\`~!@#$%^&amp;*_-+=;:'\",<>./?"
        )






#
