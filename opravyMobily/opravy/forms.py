from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Model, Brand


class ModelForm(ModelForm):
    class Meta:
        model = Model
        fields = ['name', 'znacka', 'fotka', 'cena_baterka', 'cena_displej', 'cena_stav_a', 'popis']
        labels = {'name': 'Název modelu', 'znacka': 'Značka'}
