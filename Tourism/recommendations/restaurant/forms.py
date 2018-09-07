from django.forms import ModelForm, Textarea
from django import forms


class CuisineForm(forms.Form):
    cuisine = forms.CharField(max_length=10)
   