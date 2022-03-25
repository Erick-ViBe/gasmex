from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gas_stations.views import UpdateGasStations, ListRetrieveGasStationsViewSet


router = DefaultRouter()
router.register('gas_stations', ListRetrieveGasStationsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('update_gas_stations/', UpdateGasStations.as_view(), name='update-gasstations'),
]
