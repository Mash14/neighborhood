from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    occupant_count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')
    
    @classmethod
    def delete_neighborhood(cls,id):
        cls.objects.filter(id = id).delete()

    @classmethod
    def get_neighborhood_by_id(cls,id):
        neighborhoods = cls.objects.get(id = id)
        return neighborhoods

    @classmethod
    def update_neighborhood(cls,id,new_name):
        cls.objects.filter(id = id).update(name = new_name)

    @classmethod
    def update_occupant_count(cls,id,new_count):
        cls.objects.filter(id=id).update(occupant_count = new_count)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    national_id = models.CharField(max_length=20)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=20,blank=True)
