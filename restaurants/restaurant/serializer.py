from rest_framework import serializers
from .models import Restaurant, Menu


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('name', 'address',)


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('dishes', 'day', 'restaurant')
