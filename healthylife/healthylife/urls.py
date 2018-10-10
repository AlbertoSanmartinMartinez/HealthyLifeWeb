#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import DetailView, ListView, UpdateView
from rest_framework.urlpatterns import format_suffix_patterns

from healthylifeapp import views as general_views
from healthylife import settings
from shop import views as shop_views
from shop import urls as shop_urls
from events import views as calendar_views
from events import urls as events_urls
from api import urls as api_urls
from blog import urls as blog_urls
from sportapp import urls as sportapp_urls
from nutritionapp import urls as nutritionapp_urls
from healthapp import urls as healthapp_urls
from awards import urls as awards_urls

admin.site.site_header = 'Barbastro Se Mueve'
admin.autodiscover()

urlpatterns = [

    # Pages URLS's
    path('', general_views.home, name='home'),
    path('conocenos/', general_views.know_us, name='know_us'),
    path('conocenos/colaboradores/<str:username>/', general_views.know_us_collaborator, name='collaborator'),
    path('conocenos/empresas/<str:companyname>/', general_views.know_us_company, name='company'),

    path('trabaja_con_nosotros/', general_views.work_with_our, name='work_with_our'),
    path('informacion_legal/', general_views.legal_information, name='legal_information'),
    path('contacto/', general_views.contact, name='contact'),

    # Subscribe URLS
    path('subscripcion/', general_views.subscribe, name='subscribe'),

    # Admin URLS's
    path('administracion/', admin.site.urls),

    # API Urls
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include((api_urls, 'api'), namespace='api')),

    # Blog URLS's
    path('blog/', include((blog_urls, 'blog'), namespace='blog')),

    # Search URLS's
    path('resultado_busqueda/', general_views.search, name='search'),

    # Shop URLS's
    path('tienda/', include((shop_urls, 'shop'), namespace='shop')),

    # Sport URLS's
    path('deporte/', include((sportapp_urls, 'sportapp'), namespace='sportapp')),

    # Health URLS's
    path('salud/', include((healthapp_urls, 'healthapp'), namespace='healthapp')),

    # Nutrition URLS's
    path('nutricion/', include((nutritionapp_urls, 'nutritionapp'), namespace='nutritionapp')),

    # Statistics URLS's
    path('estadisticas/', general_views.statistics, name='statistics'),

    # Awards URLS's
    path('premios/', include((awards_urls, 'awards'), namespace='awardsapp')),

    # Editor de Texto HTML URL's
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Registro URLS's
    # url(r'^mi_cuenta/$', include('django.contrib.auth.urls')),
    path('registro/', general_views.custom_registration, name='custom_register'),
    #url(r'^registro/completado/$', general_views.registration_complete, name='custom_register_complete'),
    #url(r'^registro/cancelado/$', general_views.registration_disallowed, name='registration_disallowed'),

    # Profile URLS's
    path('mi_cuenta/<str:username>/', general_views.profile, name='profile'),
    # url(r'^mi_cuenta/(?P<username>\w+)/pedidos/$', general_views.ships, name='ships'),
    path('mi_cuenta/<str:username>/deporte/', general_views.sport_profile, name='sport_profile'),
    path('mi_cuenta/<str:username>/nutricion/', general_views.nutrition_profile, name='nutrition_profile'),
    path('mi_cuenta/<str:username>/salud/', general_views.health_profile, name='health_profile'),
    #url(r'^mi_cuenta/(?P<username>\w+)/premios/$', general_views.awards_profile, name='awards_profile'),
    path('mi_cuenta/<str:username>/colaborador/', general_views.collaborator_profile, name='collaborator_profile'),

    # Calendar URLS's
    path('calendario/', include((events_urls, 'events'), namespace='calendar')),

    # Company URLS's
    #url(r'^empresas/(?P<company>\w+)/empresa/$', views.company, name='company'),

    # Collaborators URLS's
    #url(r'^colaboradores/(?P<username>\w+)/$', views.company, name='collaborators'),

    # Login URLS's
    path('acceso/', general_views.custom_login, name='custom_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('activacion/<uuid:uidb64>/<uuid:token>/', general_views.custom_activation, name='activation'),
    path('reset/', general_views.custom_reset_password, name='reset'),
    path('reset_form/<uuid:uidb64>/<uuid:token>/', general_views.custom_reset_password_form, name='reset_form'),


    #url(r'^mi_cuenta/password_change/$', auth_views.PasswordChangeView.as_view(), name='password_change'),
    #url(r'^mi_cuenta/password_change_done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #url(r'^mi_cuenta/password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #url(r'^mi_cuenta/password_reset_done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #url(r'^mi_cuenta/password_confirm/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #url(r'^mi_cuenta/password_reset_complete/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

# Format suffixes
#urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
