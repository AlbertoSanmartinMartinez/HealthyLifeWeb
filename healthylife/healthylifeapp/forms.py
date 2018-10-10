#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django import forms

from healthylifeapp import models as general_models
#from healthylifeapp.validators import UppercaseValidator
from healthylife import settings

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

#from image_cropping import ImageCropWidget


# Register Forms
class CustomPasswordResetForm(forms.ModelForm):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': u'Correo electrónico'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': u'Nueva contraseña'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': u'Confirmar contraseña'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class CustomRegisterForm(UserCreationForm):
    """
    Formulario para de registro para usuarios
    https://docs.djangoproject.com/en/2.0/ref/forms/fields/
    """
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Nombre de usuario', "size": 30 }))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': u'Correo electrónico',"size": 30}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Apellidos'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': u'Contraseña', "size": 30 }))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': u'Confirmar contraseña', "size": 30 }))
    legal = forms.BooleanField(required=True, widget=forms.CheckboxInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


# Login Forms
class CustomAuthenticationForm(AuthenticationForm):
    """
    Formulario de acceso para usuarios
    https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm
    """
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': u'Nombre usuario o correo electrónico', "size": 30}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': u'Contraseña', "size": 30 }))


class SubscriberForm(forms.ModelForm):
    email = forms.EmailField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': u'Correo electrónico', "size": 80}))

    class Meta:
        model = general_models.Subscriber
        exclude = []

# General Forms
class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(attrs={'placeholder': u'Nombre de la empresa'}))
    description = forms.CharField(label='Descripcion', required=True, widget=forms.TextInput(attrs={'placeholder': u'Descripción de la empresa'}))
    phone = forms.CharField(label='Telefono', required=True, widget=forms.TextInput(attrs={'placeholder': u'Télefono de la empresa'}))
    web = forms.CharField(label='Página web', required=False, widget=forms.TextInput(attrs={'placeholder': u'Web de la empresa'}))
    company_image = forms.ImageField(required=False, widget=forms.FileInput())

    class Meta:
        model = general_models.Company
        fields = ['company_name', 'description', 'phone', 'web', 'company_image']


class BankInformationForm(forms.ModelForm):
    bank_name = forms.CharField(label='Nombre', required=False, widget=forms.TextInput(attrs={'placeholder': u'Mi información bancaria'}))
    account = forms.CharField(label='Número de cuenta', required=False, widget=forms.TextInput(attrs={'placeholder': u'Tarjeta de crédito'}))
    month = forms.CharField(label='Mes de caducidad', required=False, widget=forms.TextInput(attrs={'placeholder': u'Més de caducidad'}))
    year = forms.CharField(label='Año de caducidad', required=False, widget=forms.TextInput(attrs={'placeholder': u'Año de caducidad'}))
    security_code = forms.CharField(label='Código de seguridad', required=False, widget=forms.TextInput(attrs={'placeholder': u'Código de seguridad'}))

    class Meta:
        model = general_models.BankInformation
        fields = ['bank_name', 'account', 'month', 'year', 'security_code']


class AddressForm(forms.ModelForm):
    address_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'placeholder': u'Mi direccón de envío'}))
    city = forms.CharField(label='Ciudad', required=False, widget=forms.TextInput(attrs={'placeholder': 'Ciudad'}))
    postal_code = forms.CharField(label='Código postal', required=False, widget=forms.TextInput(attrs={'placeholder': u'Código postal'}))
    street = forms.CharField(label='Calle', required=False, widget=forms.TextInput(attrs={'placeholder': 'Calle'}))
    number = forms.CharField(label='Número', required=False, widget=forms.TextInput(attrs={'placeholder': u'Número'}))
    floor = forms.CharField(label='Piso', required=False, widget=forms.TextInput(attrs={'placeholder': 'Piso'}))
    door = forms.CharField(label='Puerta', required=False, widget=forms.TextInput(attrs={'placeholder': 'Puerta'}))

    class Meta:
        model = general_models.Address
        fields = ['address_name', 'city', 'postal_code', 'street', 'number', 'floor', 'door']


class ContactForm(forms.Form):
    """Formulario de contacto"""
    name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder':'Nombre', "size": 40}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': u'Correo electrónico', "size": 40}))
    message = forms.CharField(max_length=500, required=True, widget=forms.TextInput(attrs={'placeholder': 'Mensaje', "size": 40}))


class CustomRegisterColaboratorForm(UserCreationForm):
    """
    Formulario para de registro de colaboradores
    """
    username = forms.CharField(max_length=100, label='Nombre de usuario', required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'placeholder': u'Correo electrónico'}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Apellidos'}))
    password1 = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput(attrs={'placeholder': u'Contraseña'}))
    password2 = forms.CharField(label='Confirmar contraseña', required=True, widget=forms.PasswordInput(attrs={'placeholder': u'Confirmar contraseña'}))
    blog_colaborator = forms.BooleanField(label=u'¿ Quieres colaborar en el blog ?', required=False)
    shop_colaborator = forms.BooleanField(label=u'¿ Quieres colaborar en la tienda ?', required=False)
    award_colaborator = forms.BooleanField(label=u'¿ Quieres colaborar con premios y recompensas ?', required=False)
    sport_colaborator = forms.BooleanField(label=u'¿ Quieres colaborar en la sección de deporte ?', required=False)
    nutrition_colaborator = forms.BooleanField(label= u'¿ Quieres colaborar en la sección de nutrición ?', required=False)
    health_colaborator = forms.BooleanField(label= u'¿ Quieres colaborar en la sección de salud ?', required=False)
    legal = forms.BooleanField(required=True, widget=forms.CheckboxInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'legal']
        help_texts = {
            'health_colaborator': u'Group to which this message belongs to',
        }


# Health forms

# Awards forms

# Profile forms
class CollaboratorProfileForm(forms.ModelForm):
    position = forms.CharField(label='Cargo', required=False, widget=forms.TextInput(attrs={'placeholder': 'Puesto'}))
    company = forms.CharField(label='Empresa', required=False, widget=forms.TextInput(attrs={'placeholder': u'Empresa'}))
    education = forms.CharField(label='Formacion', required=False, widget=forms.TextInput(attrs={'placeholder': u'Formación'}))
    extract = forms.CharField(label='Resumen', required=False, widget=forms.TextInput(attrs={'placeholder': u'Resumen sobre tí'}))
    collaborator_image = forms.ImageField(required=False, widget=forms.FileInput())

    class Meta:
        model = general_models.CollaboratorProfile
        fields = ['position', 'company', 'education', 'extract', 'collaborator_image']


class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(label='Bio', required=False, widget=forms.TextInput(attrs={'placeholder':'Bio de tu perfil'}))
    phone = forms.CharField(label='Teléfono', required=False, widget=forms.TextInput(attrs={'placeholder': u'Teléfono'}))
    profile_image = forms.ImageField(required=False, widget=forms.FileInput())


    class Meta:
        model = general_models.UserProfile
        fields = ['bio', 'phone', 'profile_image', 'cropping']
        """
        widgets = {
            'profile_image': ImageCropWidget,
        }
        """


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
    #first_name = forms.CharField(label='Nombre')
    #last_name = forms.CharField(label='Apellidos')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class SearchForm(forms.Form):
    """
    Formulario de busqueda en el blog
    """
    word = forms.CharField(label='search', widget=forms.TextInput(attrs={'placeholder': u'Escribe aquí'}))


def normalize_image(path, mode):

    from PIL import Image
    from django.core.files.storage import default_storage as storage
    from django.core.files.images import get_image_dimensions
    import os
    import json
    from healthylife.settings import MEDIA_UPLOADS_SIZES

    print("normalize view")

    print(mode)
    print(path)

    img = Image.open(path)

    #outfile = storage.open(path, "w")

    #print(outfile)
    #print(infile)

    img_width, img_height = get_image_dimensions(path)
    print(img_width)
    print(img_height)

    #modes = json.dumps(MEDIA_UPLOADS_SIZES)
    #print(modes)

    x = 0
    y = 0
    width = 0
    height = 0

    if mode == 'profile':
        normalize_width = 390
        normalize_height = 450
    elif mode == 'collaborator':
        normalize_width = 390
        normalize_height = 450
    elif mode == 'company':
        normalize_width = 160
        normalize_height = 160

    print(normalize_width)
    print(normalize_height)

    horizontal_ratio = img_width / normalize_width
    vertical_ratio = img_height / normalize_height

    if horizontal_ratio >= vertical_ratio:
        height = normalize_height * vertical_ratio
        width = img_width
    else:
        height = img_height
        width = normalize_width * horizontal_ratio

    x = (img_width - width) / 2
    y = (img_height - height) / 2

    if img_width > img_height:
        print("horizontal")
    elif img_width < img_height:
        print("vertical")
    else:
        print("cuadrado")

    print(width)
    print(height)

    cropped_image = img.crop((x, y, width, height))
    resized_image = cropped_image.resize((normalize_width, normalize_height), Image.ANTIALIAS)

    return resized_image
