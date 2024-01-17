from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('taxis', taxiViewSet)
router.register('trajectories', trajectoriesViewSet)

apiTaxi = [
    path('api/', include(router.urls))
]