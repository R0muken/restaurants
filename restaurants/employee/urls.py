from django.urls import path
from .views import UserCreateAPIView, VoteAPIView
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'menu', UserVoteViewSet)

urlpatterns = [
    path('create/', UserCreateAPIView.as_view()),
    path('vote/<int:menu_id>', VoteAPIView.as_view()),
]
#
# urlpatterns += router.urls

