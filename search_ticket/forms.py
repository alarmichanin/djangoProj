from django import forms
from .models import *
from bootstrap_datepicker_plus import DatePickerInput
from django.core.exceptions import ValidationError
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User

import datetime #for checking renewal date range.
from icecream import ic
from django.utils.translation import ugettext_lazy as _


class SearchRouteForm(forms.Form):
    """class of creating new post using modelform"""

    def clean_date(self):
        data = self.cleaned_data['date']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=1):
            raise ValidationError(_('Invalid date - renewal more than 1 weeks ahead'))

        return data

    start_point = forms.CharField(widget=forms.TextInput(attrs={"class": "validate"}))
    end_point = forms.CharField(widget=forms.TextInput(attrs={"class": "validate"}))
    date = forms.DateField(
        widget=DatePickerInput(attrs={"class": "datepicker"})
    )
