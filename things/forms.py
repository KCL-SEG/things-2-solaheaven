"""Forms of the project."""

from django import forms
from django.core.validators import RegexValidator

from .models import Thing


class ThingForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea(), 'quantity': forms.IntegerField()}

