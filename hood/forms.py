from django import forms
from django.contrib.auth.models import User
from .models import Neighborhood

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['admin'] 