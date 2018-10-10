#!/usr/local/bin/python
# coding: utf-8

from django import forms
from events import models as event_models
import datetime
from calendar import monthrange
from calendar import monthrange
from django.utils.safestring import mark_safe

idate = datetime.datetime.now()
iyear = idate.year
imonth = idate.month
iday = idate.day

# Calendar forms
"""
class TimePickerWidget(forms.TimeInput):
    def render(self, name, value, attrs=None):
        htmlString = u''
        htmlString += u'<select name="%s">' % (name)
        for i in range(0, 25):
            htmlString += ('<option value="%d:00">%d:00</option>' % (i,i))
            htmlString +='</select>'
        return mark_safe(u''.join(htmlString))
"""

class EventForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Título'}))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Descripción'}))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Lugar'}))
    #PRIVACITY = ((1, 'Público'), (2, 'Privado'))
    #privacity = forms.ChoiceField(choices=PRIVACITY, initial=1)
    #EVENT_TYPE = ((1, 'Deporte'), (2, 'Nutrición'), (3, 'Salud'))
    #type = forms.ChoiceField(choices=EVENT_TYPE, initial=1)
    # participant
    # year = iyear
    #MONTHS = ((1, 'Enero'), (3, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre'))
    #month = forms.ChoiceField(choices=MONTHS, initial=imonth)
    #DAYS = [(i, str(i)) for i in range(1, monthrange(iyear, imonth)[1]+1)]
    #day = forms.ChoiceField(choices=DAYS, initial=iday)
    #HOURS=[(i, str(i)) for i in range(0, 24)]
    #end_hour = forms.ChoiceField(choices=HOURS, initial=13)
    #start_hour = forms.ChoiceField(choices=HOURS, initial=12)
    #MINUTES=[(i, str(i)) for i in range(0, 60)]
    #end_minutes = forms.ChoiceField(choices=MINUTES, initial=0)
    #start_minutes = forms.ChoiceField(choices=MINUTES, initial=0)
    notes =forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Añade tus notas'}))

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        #self.fields['title'] = data['title']

    class Meta:
        model = event_models.Event
        # exclude = ['slug', 'owner', 'created_date', 'updated_date']
        fields = '__all__'






#
