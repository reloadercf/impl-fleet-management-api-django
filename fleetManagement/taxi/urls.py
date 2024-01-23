from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('taxis', taxiViewSet)
router.register('trajectories', trajectoriesViewSet)
router.register('last-location', LastLocationViewSet, basename='trajectories')

apiTaxi = [
    path('api/', include(router.urls))
]