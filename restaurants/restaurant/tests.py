from rest_framework.test import APITestCase
from rest_framework import status
# import mock
from django.urls import reverse
from .models import Restaurant


class TestCreateRestaurantAPI(APITestCase):

    def setUp(self):
        Restaurant.objects.create(
            name='Pub Good Friend',
            address='vul. Lesi Ukrainky 19, Lviv 79008 Ukraine')

    def test_create_new_restaurant(self):
        url = reverse('create_restaurant')
        data = {
            "name": "Taco Taco Taqueria",
            "address": "Brativ Rohatyntsiv St, 9, Lviv 79000 Ukraine"
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_view_restaurant(self):
        url = reverse('create_restaurant')
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
