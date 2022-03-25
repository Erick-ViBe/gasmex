from django.urls import path
from gas_stations.views import UpdateGasStations

urlpatterns = [
    path('update_gas_stations/', UpdateGasStations.as_view(), name='update-gasstations'),
]
