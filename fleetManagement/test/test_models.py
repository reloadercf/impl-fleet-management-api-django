import pytest
from taxi.models import Taxi, Trajectories

@pytest.mark.django_db
def test_taxi_model():
    taxi = Taxi.objects.create(plate="ABC123")
    assert taxi.plate == "ABC123"


@pytest.mark.django_db
def test_trajectories_model():
    taxi = Taxi.objects.create(plate="ABC123")
    trajectory = Trajectories.objects.create(taxi=taxi, latitude=12.345, longitude=67.890)
    assert trajectory.taxi == taxi
    assert trajectory.latitude == 12.345
    assert trajectory.longitude == 67.890
    