from django.urls import path, include
from dashboard.views import DashboardView, GasStationLocationsView, GasStationVersus


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('locations/', GasStationLocationsView.as_view(), name='gasstation-locations'),
    path('versus', GasStationVersus.as_view(), name='gasstation-versus'),
]
