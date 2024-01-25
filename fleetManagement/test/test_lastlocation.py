import pytest
from rest_framework.test import APIClient
from taxi.models import Taxi, Trajectories
from taxi.serializers import lastLocationSerializer
from taxi.views import LastLocationViewSet

@pytest.mark.django_db
class TestLastLocationViewSet:
    @pytest.fixture
    def setup_data(self):
        taxi = Taxi.objects.create(plate="ABC123")
        trajectory1 = Trajectories.objects.create(taxi=taxi, latitude=40.7128, longitude=-74.0060)
        trajectory2 = Trajectories.objects.create(taxi=taxi, latitude=34.0522, longitude=-118.2437)
        return taxi, trajectory1, trajectory2

    def test_get_last_location(self, setup_data):
        taxi, trajectory1, trajectory2 = setup_data

        client = APIClient()

        # Realizar una solicitud GET con el parámetro de taxi
        response = client.get(f'/api/last-location/?taxi={taxi.id}')

        # Verificar que la solicitud fue exitosa (código de estado 200)
        assert response.status_code == 200

        # Verificar que se devuelve la última ubicación
        assert response.data['latitude'] == trajectory2.latitude
        assert response.data['longitude'] == trajectory2.longitude

    def test_get_last_location_no_taxi_param(self):
        client = APIClient()

        # Realizar una solicitud GET sin el parámetro de taxi
        response = client.get('/api/last-location/')

        # Verificar que la solicitud fue exitosa (código de estado 200)
        assert response.status_code == 200

        # Verificar que no se devuelva ninguna ubicación
        assert response.data == {'message': 'No se proporcionó el parámetro "taxi".'}