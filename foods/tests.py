
from urllib import response
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse,resolve
from .models import Food,Reserveation,Comment
from django.test import SimpleTestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .views import ReserveationList




class FoodTests(TestCase):
    def setUp(self):
        
        
        self.Food = Food.objects.create(
            name = 'a good name',
            description='food  description',
            rate='food rate',
            price='food price',
            time='food time',   
        )

def test_string_representation(self):
    Food = Food(name='a good name')
    self.assertEqual(Food.title, str(Food))

    
    def test_food_content(self):
        self.assertEqual(f"{self.food.name}", "a good title")
        self.assertEqual(f"{self.food.description}", "a good  description")
        self.assertEqual(f"{self.food.rate}", "a good rate")
        self.assertEqual(f"{self.food.price}", "a good price")
        self.assertEqual(f"{self.Food.time}", "a good time")
        



        


   
class ApiUrlTests(SimpleTestCase):

    def test_get_ReserveationList_is_resolve(self):
        url=reverse('ReserveationList')
        print(resolve(url).func)
        self.assertEqual(resolve(url).func.view_class.ReserveationList)
        print(url)


# class FoodListApiViewTests(APITestCase):
#     FoodList_url=reverse('foodList')

#     def setUp(self) :
#         self.user=User.objects.create_user(
#             username='admin',
#             password="1234567")
            
#         self.token=Token.objects.create(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token'+self.token.key)


# def test_get_FoodList(self):
#         response=self.client.get(self.FoodList_url)
#         self.assertEqual(response.status_code,status.HTTP_200_OK)

#         self.Food = Food.objects.create(
#             name = 'food name',
#             description=' food description',
#             rate='food rate',
#             price='food price',
            
#             )
     
#        