#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import django_heroku

from easy_thumbnails.conf import Settings as thumbnail_settings
from dj_database_url import parse as dburl
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r6zfm1@g^!qz8r@v!w*kl^z&s0&oxf1g5u5md!^1tv4-!xsbem'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'healthylifeweb.herokuapp.com',
    '127.0.0.1'
]

"""
EMAIL_HOST = 'mail.hostingaragon.info'
EMAIL_HOST_USER = 'info@preconcebido.com'
EMAIL_HOST_PASSWORD = 'Motoscoot.es7620'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
"""

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'healthylifeapp',
    'nutritionapp',
    'sportapp',
    'healthapp',
    'blog',
    'shop',
    'events',
    'awards',
    'api',
    'rest_framework',
    'ckeditor',
    #'corsheaders',
    'image_cropping',
    'easy_thumbnails',
    # 'datetimewidget',
)

#MIDDLEWARE_CLASSES = (
MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    #'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'healthylife.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                    os.path.join(BASE_DIR, "templates"),
                    BASE_DIR + '/templates/blog/',
                    BASE_DIR + '/templates/shop/',
                    BASE_DIR + '/templates/sport/',
                    BASE_DIR + '/templates/health/',
                    BASE_DIR + '/templates/nutrition/',
                    BASE_DIR + '/templates/registration/',
                    BASE_DIR + '/templates/awards/',
                    BASE_DIR + '/templates/calendar/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'healthylife.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
#DATABASE = {'default': config('DATABASE_URL', default=default_dburl, cast=dburl), }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'healthylifedb',
        'USER': 'dbadminuser',
        'PASSWORD': 'Barbastro2017',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

#ACCOUNT_ACTIVATION_DAYS = 1
#REGISTRATION_AUTO_LOGIN = True
#SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ********** STATIC FILES **********

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    #'static',
]
"""
STATICFILES_FINDERS = [
       "django.contrib.staticfiles.finders.FileSystemFinder",
       "django.contrib.staticfiles.finders.AppDirectoriesFinder"
]
"""
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
#STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = '/media/'

MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, "media"),
    # BASE_DIR + '/photos/',
]

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

LOGIN_URL = 'custom_login'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = 'home'

# Authentication Backends for Django and Admin
AUTHENTICATION_BACKENDS = [
    'healthylifeapp.backend.CustomBackend',
    'django.contrib.auth.backends.ModelBackend',
]

REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
    ),
    # Authentication Backends for DRF and Ionic
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        #'rest_framework.authentication.SessionAuthentication',
        #'rest_framework.authentication.BasicAuthentication',
    ),
}

CKEDITOR_UPLOAD_PATH = 'ckeditor/'
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'full': {
        'toolbar': 'Full'
    },
    'basic': {
        'toolbar': 'Basic'
    }
}

# CORS, to allow all origin to the api during development
# https://github.com/zestedesavoir/django-cors-middleware
"""
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1',
    '192.168.1.21',
    '172.16.120.113'
    '192.168.1.101',
)

CORS_ORIGIN_ALLOW_ALL = True

CORS_URLS_ALLOW_ALL_REGEX = (

)

CORS_URLS_ALLOW_ALL = True
"""

# ********** STATIC FILES **********
X_APP_ID = 'bcd58f59'
X_APP_KEY = '1a3868de0641119014fc38bb848af63e'

# SHOPPING CART
CART_SESSION_ID = 'cart'

# ********** CROP MEDIA FILES **********

THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

#IMAGE_CROPPING_BACKEND = 'image_cropping.backends.easy_thumbs.EasyThumbnailsBackend'
#IMAGE_CROPPING_BACKEND_PARAMS = {}

# ********** PASSWORD VALIDATORS **********

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'healthylifeapp.validators.NumberValidator',
        'OPTIONS': {
            'min_digits': 1,
        }
    },
    {
        'NAME': 'healthylifeapp.validators.UppercaseValidator',
        'OPTIONS': {
            'min_uper': 1,
        }
    },
    {
        'NAME': 'healthylifeapp.validators.LowercaseValidator',
        'OPTIONS': {
            'min_lower': 1,
        }
    },
    {
        'NAME': 'healthylifeapp.validators.SymbolValidator',
        'OPTIONS': {
            'min_char': 1,
        }
    }
]

#django_heroku.settings(locals())
