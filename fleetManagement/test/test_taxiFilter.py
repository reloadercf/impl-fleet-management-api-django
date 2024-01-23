import pytest
from rest_framework import status
from django.urls import reverse
from taxi.models import Taxi, Trajectories

@pytest.mark.django_db
class TestTrajectoriesViewSet:
    @pytest.fixture
    def setup_data(self):
        taxi = Taxi.objects.create(id="1", plate='ffff')
        trajectory = Trajectories.objects.create(taxi_id="1", date="2024-01-01", latitude="2343.23423", longitude="2342.234234")
        return taxi, trajectory
    
    def test_trajectories_filter_by_date(self, setup_data, client):
        trajectory = setup_data
        response = client.get(reverse('trajectories-list') + f'?taxi=1')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 1
        assert response.json()[0]['taxi'] == 1

    def test_trajectories_filter_by_nonexistent_id(self, client):
        response = client.get(reverse('trajectories-list') + '?id=999')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 0