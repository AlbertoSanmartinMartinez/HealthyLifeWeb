#!/usr/local/bin/python
# coding: utf-8

from django import forms
from nutritionapp import models as nutrition_models

# Nutrition forms
class NutritionFilter(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Escribe alimentos', 'id': 'name'}))
    # required_css_class = ''
    # error_css_class = ''

    # creo que el modelo no hace falta
    class Meta:
        model = nutrition_models.Food
        exclude = ['description', 'date']
