from django.db import models
from datetime import datetime

class Taxi(models.Model):
    plate   =   models.CharField(max_length=80)
    def __str__(self):
        return self.plate
    
class Trajectories(models.Model):
    taxi        =   models.ForeignKey('taxi.Taxi', related_name='taxi_plate', on_delete=models.CASCADE)
    date        =   models.DateTimeField(default=datetime.now)
    latitude    =   models.FloatField()
    longitude   =   models.FloatField()