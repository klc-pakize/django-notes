from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class Car(models.Model):

    GEAR = (
        ('a', 'automatic'),
        ('m', 'manuel')
    )

    plate_number = models.CharField(max_length = 15, unique = True)
    brand = models.CharField(max_length = 15)
    model = models.CharField(max_length = 20)
    rent_per_day = models.DecimalField(
        max_digits = 6,  # max_digits = We specify how many digits the number will have at most.
        decimal_places = 2,  # decimal_places = We specify the maximum number of digits after the comma.
        validators = [MinValueValidator(50)],  # MinValueValidator = We specify the minimum number to be entered in this field, not less than the number we specified.
    )
    gear = models.CharField(max_length = 1, choices = GEAR)
    year = models.SmallIntegerField()
    availability = models.BooleanField(default = True)

    def __str__(self):
        return f" {self.plate_number} {self.model} {self.brand} "
    