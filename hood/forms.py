from django import forms
from django.contrib.auth.models import User
from .models import Neighborhood, Post,UserProfile,Business

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