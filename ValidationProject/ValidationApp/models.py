from django.db import models
from datetime import date


# new car
class NewCarModel(models.Model):
    make = models.CharField(max_length=50, default='')
    modelYear = models.IntegerField(default=2019)
    mpg = models.IntegerField(default=20)

    def __str__(self):
        return self.make