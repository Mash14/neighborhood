from django import forms
from django.contrib.auth.models import User
from .models import Neighborhood,UserProfile

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['admin'] 


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']