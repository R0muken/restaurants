from django.db import models, transaction
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    username = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True)
    email = models.EmailField(
        max_length=100,
        unique=True,
        validators=[validate_email])
    first_name = models.CharField(
        max_length=30,
        blank=True)
    last_name = models.CharField(
        max_length=30,
        blank=True)
    restaurant = models.ForeignKey(
        to='restaurant.Restaurant',
        on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return str(f'{self.first_name} {self.last_name}')


class EmployeeVote(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        default=None)
    date = models.DateField(auto_now_add=True)
    has_voted = models.BooleanField(default=False)
    menu = models.ForeignKey(
        to='restaurant.Menu',
        on_delete=models.CASCADE, null=True)