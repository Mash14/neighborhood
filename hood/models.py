from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    occupant_count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,to_field='username' ,on_delete=models.CASCADE,editable=False,null=True)