from django import forms
from django.contrib.auth.models import User
from .models import Neighborhood, Post,UserProfile,Business,Services

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['admin'] 


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','profile','pub_date']

class UpdateServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['neighborhood','police_station','station_number','health_center','center_number']