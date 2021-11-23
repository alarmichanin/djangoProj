from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# from captcha.fields import CaptchaField
from django .core import validators


class SearchRouteForm(forms.ModelForm):
    """ class of creating new post using modelform """
 
    class Meta:
        model = Route
        # rewrite static photo field

        fields = ["start_point", "end_point"]
        widgets = {

            'start_point': forms.TextInput(attrs={'class': 'form-control'}),
            'end_point': forms.Textarea(attrs={'class': 'form-control'}),
        }
