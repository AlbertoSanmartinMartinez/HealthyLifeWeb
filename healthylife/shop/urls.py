# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url
from django.urls import path, include, re_path
from django.conf.urls.static import static
from shop import views as shop_views
from django.conf import settings

urlpatterns = [

    # Products Shop Urls
    path('productos/', shop_views.product_list, name='product_list'),
    path('productos/<str:product_slug>/', shop_views.product_detail, name='product_detail'),
    path('productos/<str:product_slug>)/comentario', shop_views.add_review, name='add_review'),

    # Category Urls
    path('categorias/<str:shop_category_slug>/', shop_views.product_list, name='product_list_category'),

    #Search Urls
    path('productos/', shop_views.product_list, name='shop_search'),

    # Payments Urls
    path('pago/realizado', shop_views.payment_done, name='payment_done'),
    path('pago/cancelado', shop_views.payment_canceled, name='payment_canceled'),

    # Shipping Urls
    path('direccion_envio/', shop_views.address_checkout, name='address_checkout'),
    path('metodo_envio/', shop_views.shipping_checkout, name='shipping_checkout'),
    path('metodo_pago/', shop_views.payment_checkout, name='payment_checkout'),

    path('pedido/', shop_views.order_checkout, name='order_checkout'),

    # ShopingChart Urls
    path('carrito/', shop_views.shoppingcart, name='shoppingcart_detail'),
    path('carrito/nuevo/<int:product_id>/', shop_views.cartAdd, name='shoppingcart_add'),

    #Profile Urls
    path('mi_cuenta/<str:username>/pedidos/', shop_views.ships, name='ships'),

]
