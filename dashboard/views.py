from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "dashboard/gasmex.html"


class GasStationLocationsView(TemplateView):
    template_name = "dashboard/gas_station_locations.html"


class GasStationVersus(TemplateView):
    template_name = "dashboard/gas_stations_versus.html"
