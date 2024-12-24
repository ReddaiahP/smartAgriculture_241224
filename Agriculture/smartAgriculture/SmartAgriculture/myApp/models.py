
from django.db import models


class Agriculture(models.Model):
    motor = models.CharField(max_length=10)
    temp = models.IntegerField()
    humidity = models.IntegerField()
    soil_moisture = models.IntegerField()

