from django.shortcuts import render
from rest_framework import status, generics, mixins, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from restaurant.models import Menu
from .models import Employee, EmployeeVote
from .serializers import UserSerializer, VoteSerializer

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


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = Employee.objects.all()


class VoteAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, menu_id):
        menu = Menu.objects.get(id=menu_id)
        employee = Employee.objects.get(id=request.user.id)

        if EmployeeVote.objects.filter(
            date=timezone.now().date(),
            employee_id=employee.id
            ):
            res = {
                'data': 'You already voted',
                "success": False
            }
            return Response({'data': res}, status=status.HTTP_200_OK)
        else:
            if menu.restaurant_id == request.user.restaurant_id:
                menu.votes += 1
                menu.save()
            vote = EmployeeVote.objects.create(
                employee=employee,
                has_voted=True,
                menu=menu
            )
            serializer = VoteSerializer(menu, many=False)
            res = {
                'data': serializer.data,
                "success": True
            }
            return Response({'data': res}, status=status.HTTP_200_OK)



