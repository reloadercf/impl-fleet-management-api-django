from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class taxiViewSet(viewsets.ModelViewSet):
    queryset            = Taxi.objects.all()
    serializer_class    = taxiSerializer

class trajectoriesViewSet(viewsets.ModelViewSet):
    queryset            = Trajectories.objects.all()
    serializer_class    = trajectoriesSerializer
    filter_backends     = [DjangoFilterBackend]
    filterset_fields    = ('taxi', 'date')
    

def index(request):
    return render(request, 'taxi/index.html')
