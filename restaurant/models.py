from django.db import models


# Create your models here.
class Meal(models.Model):
    # Name of the meal.
    name = models.CharField('Name of Meal', max_length=100)

    # Description for our meal.
    # Optional field
    description = models.TextField('Description of Meal', blank=True, null=True)

    # Stores the price of the meal.
    price = models.DecimalField('Price ($)', max_digits=10, decimal_places=2)

    # Available store the boolean true or false depending on whether the meal is available
    # online
    available = models.BooleanField('Available', default=False)

