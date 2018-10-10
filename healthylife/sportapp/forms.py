#!/usr/local/bin/python
# coding: utf-8

from django import forms
from sportapp import models as sport_models

# Sport forms
class SportSessionForm(forms.ModelForm):
    class Meta:
        model = sport_models.SportSession
        fields = ['name', 'sport_type', 'date', 'duration', 'calories']


class SportTypeForm(forms.ModelForm):
    class Meta:
        model = sport_models.SportType
        fields = []


class SportFilter(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Escribe alimentos', 'id': 'name'}))

    def __init__(self, *args, **kwargs):
        super(SportFilter, self).__init__(*args, **kwargs)
        self.fields['type'] = forms.ModelChoiceField(
            label='Tipo',
            required=False,
            queryset=sport_models.SportType.objects.all())
