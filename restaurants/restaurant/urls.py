from django.urls import path
from rest_framework import routers

from .views import RestaurantCreateAPIView, MenuCreateAPIView, MenuViewSet

router = routers.SimpleRouter()
router.register(r'menu/(?P<restaurant_id>\d+)', MenuViewSet, basename='menu')


urlpatterns = [
    path('', RestaurantCreateAPIView.as_view(), name='create_restaurant'),
    path('menu/create', MenuCreateAPIView.as_view()),
]

urlpatterns += router.urls
