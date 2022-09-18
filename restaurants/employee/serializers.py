from rest_framework import serializers

from restaurant.models import Menu
from .models import Employee, EmployeeVote


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('username', 'email', 'first_name', 'last_name',
                  'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = Employee(**validated_data)
        user.set_password(password)
        user.save()
        return user


class VoteSerializer(serializers.ModelSerializer):
    # menu = serializers.SerializerMethodField()
    class Meta:
        model = Menu
        fields = ('votes', 'dishes')
