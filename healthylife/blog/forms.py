#!/usr/local/bin/python
# coding: utf-8

from django import forms

#from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget

from blog import models as blog_models

# Blog forms
class PostForm(forms.ModelForm):

    class Meta:
        model = blog_models.Post
        fields = []


class PostFilter(forms.ModelForm):
    title = forms.CharField(label='Título', required=False, widget=forms.TextInput(attrs={'placeholder': 'Busca'}))
    #minimum_date = forms.DateField(label='fecha mínima', required=False, widget=forms.DateInput(attrs={ 'placeholder': u'Fecha mínima'}))
    #maximum_date = forms.DateField(label='fecha máxima', required=False, widget=forms.DateInput(attrs={'placeholder': u'Fecha máxima'}))
    ORDER_BY = ((1, ("Más antiguos primero")), (2, ("Más recientes primero")))
    order_by = forms.ChoiceField(choices = ORDER_BY, label="Ordenar", initial=1, widget=forms.Select(), required=False)

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(
            label='Categoría',
            required=False,
            queryset=blog_models.Category.objects.all())
        """
        self.fields['tags'] = forms.ModelChoiceField(
            widget=forms.CheckboxSelectMultiple,
            label='Etiquetas',
            required=False,
            queryset=blog_models.Tag.objects.all())
        """

    class Meta:
        model = blog_models.Post
        exclude = ['description', 'content', 'updated_date', 'tags', 'created_date']


class CommentForm(forms.ModelForm):

    class Meta:
        model = blog_models.Comment
        fields = '__all__'


class CommentFormAuthenticated(forms.Form):
    title = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'id': 'comment_title', 'placeholder': u'Título del comentario'}))
    content = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'id': 'comment_content', 'placeholder': 'Contenido del comentario'}))

    """
    class Meta:
        model = blog_models.Comment
        fields = ['title', 'content']
    """

class CommentFormNotAuthenticated(forms.Form):
    name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'id': 'comment_title', 'placeholder':'Nombre'}))
    email = forms.EmailField(label='', required=True, widget=forms.EmailInput(attrs={'id': 'comment_email', 'placeholder': u'Correo electrónico'}))
    title = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'id': 'comment_title', 'placeholder': u'Título del comentario'}))
    content = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'id': 'comment_content', 'placeholder': 'Contenido del comentario'}))

    """
    class Meta:
        model = blog_models.Comment
        fields = ['name', 'title', 'content', 'email']
    """





    #
