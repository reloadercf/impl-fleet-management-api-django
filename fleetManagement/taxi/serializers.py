from rest_framework import serializers
from .models import Taxi,Trajectories

class taxiSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Taxi
        fields  = '__all__'

class trajectoriesSerializer(serializers.ModelSerializer):
    taxi        = serializers.PrimaryKeyRelatedField(
                  queryset = Taxi.objects.all(),
                  required = True,
                  many     = False)
    class Meta:
        model   = Trajectories
        fields  = '__all__'