from time import time
from django.db import models

# Create your models here.

class health(models.Model):
    thermo = models.FloatField(max_length=10)
    heartrate = models.IntegerField()
    time = models.DateTimeField(max_length=20)


class gas(models.Model):
    gas_voltage_level = models.FloatField(max_length=10)
    LPG_ppm = models.FloatField(max_length=10)
    CO_ppm = models.FloatField(max_length=10)    
    time = models.DateTimeField(max_length=20)

class temp_humid(models.Model):
    temp=models.FloatField(max_length=10)
    humid=models.FloatField(max_length=10)
    time = models.DateTimeField(max_length=20)