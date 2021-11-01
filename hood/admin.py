from django.contrib import admin
from .models import Neighborhood,Business,UserProfile,Police,Health

# Register your models here.

admin.site.register(Neighborhood)
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Police)
admin.site.register(Health)