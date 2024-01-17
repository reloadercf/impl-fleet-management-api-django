from rest_framework import serializers
from .models import Taxi,Trajectories

class taxiSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Taxi
        fields  = '__all__'

class trajectoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Trajectories
        fields  = '__all__'