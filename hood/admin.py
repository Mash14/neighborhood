from django.contrib import admin
from .models import Neighborhood,Business,UserProfile

# Register your models here.

admin.site.register(Neighborhood)
admin.site.register(UserProfile)
admin.site.register(Business)
