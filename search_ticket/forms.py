from django import forms
from .models import *
# from django.core.exceptions import ValidationError
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User


class SearchRouteForm(forms.Form):
    """ class of creating new post using modelform """

    start_point = forms.CharField(
        widget=forms.TextInput(attrs={"class": "validate"}))
    end_point = forms.CharField(
        widget=forms.TextInput(attrs={"class": "validate"}))
    # receive_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control ','readonly':True }),
    # )

    # class Meta:
    #     # rewrite static photo field

    #     fields = ["start_point", "end_point"]
    #     widgets = {

    #         'start_point': forms.TextInput(attrs={'class': 'form-control'}),
    #         'end_point': forms.TextInput(attrs={'class': 'form-control'}),
    #     }
