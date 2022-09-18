from django.db import models

DAY_CHOICES = (
    (0, 'day'),
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
)


class Restaurant(models.Model):
    name = models.CharField(
        max_length=55,
        db_index=True)
    address = models.CharField(
        max_length=55,
        null=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    dishes = models.CharField(
        max_length=200,
        null=True)
    day = models.IntegerField(
        default=0,
        choices=DAY_CHOICES)
    restaurant = models.ForeignKey(
        'Restaurant',
        on_delete=models.PROTECT,
        null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.dishes
