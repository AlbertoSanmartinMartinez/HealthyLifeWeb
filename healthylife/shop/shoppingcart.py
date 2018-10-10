# -*- coding: utf-8 -*-

from decimal import Decimal
from django.conf import settings
from shop import models as shop_models
from django.shortcuts import render, get_object_or_404

class ShoppingCart(object):

    def __init__(self, session):
        """
        """
        self.session = session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    #def add(self, product, quantity=1, update_quantity=False):
    def add(self, product, quantity):
        """
        Function that add product to shoppingcart
        If it's the first product added, we to create the shoppingcart object in the data base
        """
        print("funcion añadir del carrito")
        print("id producto " + str(product.id))
        print("cantidad " + str(quantity))

        product_id = str(product.id)

        if product.id not in self.cart: # esto no funciona
            print("el producto no esta en el carrito")
            self.cart[product_id] = {'quantity': quantity, 'price': str(product.price)}

        if not shop_models.ShopingChart.objects.filter(code=str(self.session.session_key)):
            print("el carrito no existe, lo creamos")
            print(self.session.session_key)
            print(self.cart)
            shoppingcart = shop_models.ShopingChart.objects.create(code=str(self.session.session_key))

        shop_models.ShopingChart.objects.filter(code=str(self.session.session_key)).update(products=self.cart)
        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    def remove(self, product):
        product_id = str(product.id)
        del self.cart[product_id]
        shop_models.ShopingChart.objects.filter(code=str(self.session.session_key)).update(products=self.cart)
        self.save()

    """
    def update(self, product, quantity):
        product_id = str(product.id)
        self.cart[product_id] = {'quantity': quantity, 'price': str(product.price)}
        shop_models.ShopingChart.objects.filter(code=str(self.session.session_key)).update(products=self.cart)
        self.save()
    """

    def __iter__(self):
        product_ids = self.cart.keys()
        products = shop_models.Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['totalPrice'] = item['price'] * item['quantity']
            yield item


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def getTotalPrice(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


    def clear(self):
        shoppingcart = get_object_or_404(shop_models.ShopingChart, code=str(self.session.session_key))
        shop_models.Order.objects.create(
            code=shoppingcart.code)
        shoppingcart.delete()
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True


    def updateShoppingCart(self):
        pass
