
from rest_framework import generics, mixins
from rest_framework.viewsets import GenericViewSet
from .models import Restaurant, Menu
from .serializer import RestaurantSerializer, MenuSerializer
from django.utils import timezone


day = timezone.now().date()
day = day.strftime("%A")
if day == 'Monday':
    day = 1
elif day == 'Tuesday':
    day = 2
elif day == 'Wednesday':
    day = 3
elif day == 'Thursday':
    day = 4
elif day == 'Friday':
    day = 5
elif day == 'Saturday':
    day = 6
elif day == 'Sunday':
    day = 7


class RestaurantCreateAPIView(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    # permission_classes = (permissions.IsAdminUser,)


class MenuCreateAPIView(generics.CreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    # permission_classes = (IsAdminUser,)


class MenuViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin, GenericViewSet):
    serializer_class = MenuSerializer

    def get_queryset(self):
        restaurant = self.kwargs['restaurant_id']
        return Menu.objects.filter(restaurant=restaurant, day=day)
