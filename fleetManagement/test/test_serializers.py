import pytest
from taxi.serializers import taxiSerializer, trajectoriesSerializer
from taxi.models import Taxi

@pytest.mark.django_db
def test_taxi_serializer():
    data = {'plate': 'ABC123'}
    serializer = taxiSerializer(data=data)
    assert serializer.is_valid() is True
    

@pytest.mark.django_db
def test_trajectories_serializer():
    taxi = Taxi.objects.create(plate="ABC123")
    data = {'taxi': taxi.pk, 'latitude': 12.345, 'longitude': 67.890}
    serializer = trajectoriesSerializer(data=data)
    assert serializer.is_valid() is True
