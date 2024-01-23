from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets,generics
from django_filters.rest_framework import DjangoFilterBackend

class taxiViewSet(viewsets.ModelViewSet):
    queryset            = Taxi.objects.all()
    serializer_class    = taxiSerializer

class trajectoriesViewSet(viewsets.ModelViewSet):
    queryset            = Trajectories.objects.all()
    serializer_class    = trajectoriesSerializer
    filter_backends     = [DjangoFilterBackend]
    filterset_fields    = ('taxi', 'date')

class LastLocationViewSet(viewsets.ModelViewSet):
    serializer_class    = lastLocationSerializer
    def get_queryset(self):
        queryset = Trajectories.objects.all()
        taxi = self.request.query_params.get('taxi')
        last_location = []
        if taxi is not None:
            queryset = queryset.filter(taxi_id=taxi).order_by('-date').first()
            last_location.append(queryset)
            return last_location
    
def index(request):
    return render(request, 'taxi/index.html')
