from django.db import models

class Taxi(models.Model):
    plate   =   models.CharField(max_length=80)
    def __str__(self):
        return self.plate
    
class Trajectories(models.Model):
    taxi        =   models.ForeignKey('taxi.Taxi', related_name='taxi_plate', on_delete=models.CASCADE)
    date        =   models.DateField(auto_now_add=True)
    latitude    =   models.DecimalField(max_digits=9, decimal_places=6)
    longitude   =   models.DecimalField(max_digits=9, decimal_places=6)