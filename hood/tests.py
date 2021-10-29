from django.test import TestCase
from .models import Neighborhood,UserProfile,Post
from django.contrib.auth.models import User

# Create your tests here.

class NeighborhoodTestClass(TestCase):

    def setUp(self):
        # self.admin = 
        self.new_neighborhood = Neighborhood(name = 'Marurui',location = 'Roysambu', occupant_count = 20000)
        self.new_neighborhood.save()

    def tearDown(self):
        Neighborhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighborhood,Neighborhood))

    def test_save_method(self):
        self.new_neighborhood.save_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood)>0)

    def test_delete_method(self):
        self.new_neighborhood.save_neighborhood()
        self.new_neighborhood.delete_neighborhood(id = self.new_neighborhood.id)
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) == 0)

    def test_update_neighborhood_method(self):
        self.new_neighborhood.save_neighborhood()
        neighborhood_id = self.new_neighborhood.id
        Neighborhood.update_neighborhood(neighborhood_id, 'Thome')
        self.new_neighborhood.refresh_from_db()
        self.assertEquals(self.new_neighborhood.name, 'Thome')

    def test_update_count_method(self):
        self.new_neighborhood.save_neighborhood()
        neighborhood_id = self.new_neighborhood.id
        Neighborhood.update_occupant_count(neighborhood_id,20002)
        self.new_neighborhood.refresh_from_db()
        self.assertEquals(self.new_neighborhood.occupant_count,20002)

    def test_get_neighborhood_by_id(self):
        self.new_neighborhood.save_neighborhood()
        search_neighborhood = self.new_neighborhood.get_neighborhood_by_id(self.new_neighborhood.id)
        searched_neighborhood = Neighborhood.objects.filter(id=self.new_neighborhood.id)
        self.assertTrue(searched_neighborhood,search_neighborhood)


class UserprofileTestClass(TestCase):

    def setUp(self):
        self.new_neighborhood = Neighborhood(name = 'Marurui',location = 'Roysambu', occupant_count = 20000)
        self.new_neighborhood.save()

        self.user = User(username = 'mash', email = 'mash@gmail.com', password = 'test')
        self.user.save()

        self.new_userProfile = UserProfile(user = self.user,name = 'Alan',profile_pic = 'image1.png',national_id = '37396037',neighborhood = self.new_neighborhood,email_address = 'mash@gmail.com')
        self.new_userProfile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_userProfile,UserProfile))

    def test_save_method(self):
        self.new_userProfile.save_userProfile()
        user = UserProfile.objects.all()
        self.assertTrue(len(user)>0)