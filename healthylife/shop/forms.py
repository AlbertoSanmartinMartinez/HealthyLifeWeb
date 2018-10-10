#!/usr/local/bin/python
# coding: utf-8

from django import forms
from shop import models as shop_models
#from shop.templatetags import calculateStockItem

# General Forms
class SearchForm(forms.Form):
    """Formulario de busqueda"""
    word = forms.CharField(label='', widget=forms.TextInput(attrs={'id': 'search_word', 'placeholder':'Busca lo que quieras', "size": 50, 'class': 'form-control'}))


class PaymentCheckout(forms.Form):
    credir_card_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Número de tarjeta'}))
    credir_card_date = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Número de tarjeta'}))
    credir_card_code = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Número de tarjeta'}))


class ProductFilter(forms.ModelForm):
    #category = forms.ChoiceField(label='Categoria', required=False)
    #category = forms.ModelForm()
    name = forms.CharField(label='Nombre', required=False, widget=forms.TextInput(attrs={'placeholder':'Busca un producto'}))
    minimum_price = forms.DecimalField(label='Precio minimo', required=False, max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'placeholder': 'Mínimo'}))
    maximum_price = forms.DecimalField(label='Precio maximo', required=False, max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'placeholder': 'Máximo'}))
    # https://www.w3schools.com/howto/howto_js_rangeslider.asp
    ORDER_BY = ((1, ("Precio de menor a mayor")), (2, ("Precio de mayor a menor")))
    order_by = forms.ChoiceField(choices = ORDER_BY, label="Ordenar", initial=1, widget=forms.Select(), required=False)
    #without_stock = forms.BooleanField(label='Sin stock', required=False, initial=False)
    with_discount = forms.BooleanField(label='Con descuento', required=False)

    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(
            label='Categoria',
            required=False,
            queryset=shop_models.Category.objects.all())

    class Meta:
        model = shop_models.Product
        #include = ['category', 'name', 'price']
        exclude = ['description', 'slug', 'price', 'album', 'size', 'weight', 'status', 'discount', 'stock']


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(0, 26)]

class ShoppingCartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, help_text = 'Uds.')


REVIEW_MARK_CHOICES = [(i, str(i)) for i in range(0, 11)]
# Comment Forms
class ReviewFormAuthenticated(forms.ModelForm):
    title = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'id': 'comment_title', 'placeholder':'Título del comentario'}))
    content = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'id': 'comment_content', 'placeholder':'Contenido del comentario'}))
    mark = forms.TypedChoiceField(required=True, choices=REVIEW_MARK_CHOICES, coerce=int, help_text = '', label='Puntuación')

    class Meta:
        model = shop_models.Review
        fields = ['title', 'content', 'mark']


class ReviewFormNotAuthenticated(forms.ModelForm):
    name = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'id': 'comment_title', 'placeholder':'Nombre'}))
    email = forms.EmailField(required=True, label='', widget=forms.EmailInput(attrs={'id': 'comment_email', 'placeholder': 'Eamil'}))
    title = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'id': 'comment_title', 'placeholder':'Título del comentario'}))
    content = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'id': 'comment_content', 'placeholder':'Contenido del comentario'}))
    mark = forms.TypedChoiceField(required=True, choices=REVIEW_MARK_CHOICES, coerce=int, help_text = '', label='Puntuación')

    class Meta:
        model = shop_models.Review
        fields = ['name', 'mark', 'title', 'content', 'email']
#
