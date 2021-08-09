from django import forms
from django.core import validators
from django.core.validators import RegexValidator

class SendForm(forms.Form):
    arquivo_heif = forms.CharField(
        max_length='5',
        required=True,
    )