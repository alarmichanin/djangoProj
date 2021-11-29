from django import forms
from .models import *
from bootstrap_datepicker_plus import DatePickerInput
# from django.core.exceptions import ValidationError
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User


class SearchRouteForm(forms.Form):
    """class of creating new post using modelform"""

    start_point = forms.CharField(widget=forms.TextInput(attrs={"class": "validate"}))
    end_point = forms.CharField(widget=forms.TextInput(attrs={"class": "validate"}))
    # date = forms.DateField(
    #     widget=DatePickerInput(format='%m/%d/%Y')
    # )
