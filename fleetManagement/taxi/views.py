from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

class taxiViewSet(viewsets.ModelViewSet):
    queryset            = Taxi.objects.all()
    serializer_class    = taxiSerializer

class trajectoriesViewSet(viewsets.ModelViewSet):
    queryset            = Trajectories.objects.all()
    serializer_class   = trajectoriesSerializer

def index(request):
    return render(request, 'taxi/index.html')
